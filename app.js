
import { FaceLandmarker, FilesetResolver } from '@mediapipe/tasks-vision';
import * as THREE from 'three'; // Import Three.js module (optional if global, but safer)
import { FaceLandmarker, FilesetResolver } from '@mediapipe/tasks-vision';
// --- Global Variables ---
let faceLandmarker;
let video;
let scene, camera, renderer;
let lasers = {};
let lastVideoTime = -1;

// Landmarks for the eye centers (Irises)
const RIGHT_EYE_LANDMARK_INDEX = 468;
const LEFT_EYE_LANDMARK_INDEX = 473;

// --- Setup Functions (Copied/Modified from your initial script) ---

// 1. Setup Camera and Video Element
async function setupCamera() {
    video = document.getElementById('video-feed');
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;

    return new Promise((resolve) => {
        video.onloadedmetadata = () => {
            video.play();
            // Set canvas size to match video size
            const canvas = document.getElementById('ar-canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            resolve();
        };
    });
}

// 2. Setup MediaPipe Face Mesh
async function setupFaceMesh() {
    const filesetResolver = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/wasm"
    );

    faceLandmarker = await FaceLandmarker.create(filesetResolver, {
        baseOptions: {
            modelAssetPath: `https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker_gpu/float16/1/face_landmarker_gpu.task`,
            delegate: "GPU"
        },
        outputFacialTransformationMatrix: true, // Crucial for head rotation
        runningMode: "VIDEO",
        numFaces: 1
    });
}

// 3. Setup Three.js Scene and Camera
function setupThreeJS() {
    const canvas = document.getElementById('ar-canvas');
    const width = canvas.width;
    const height = canvas.height;

    renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(window.devicePixelRatio);

    scene = new THREE.Scene();

    // Use a PerspectiveCamera that roughly matches the webcam's FOV.
    // NOTE: The Three.js camera will NOT render the video, only the AR elements.
    // We choose a scale where 1 unit = roughly 10cm in the real world (arbitrary for AR).
    const fov = 45; 
    const aspect = width / height;
    const near = 0.1;
    const far = 1000;
    camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
    camera.position.z = 5; // Place camera 5 units (e.g., 50cm) away from the origin (where the face starts).
}

// 4. Create the Laser Mesh Objects
function createLaserEffects() {
    // Create a thin red cylinder/tube geometry
    const laserGeometry = new THREE.CylinderGeometry(0.01, 0.01, 10, 8);
    // Move the pivot point to the bottom (where it meets the eye)
    laserGeometry.translate(0, 5, 0); 

    // Material with emissive color for a glowing effect
    const laserMaterial = new THREE.MeshBasicMaterial({ 
        color: 0xff0000, 
        emissive: 0xff0000,
        transparent: true,
        opacity: 0.8
    });

    // Create the two laser beams
    const leftLaser = new THREE.Mesh(laserGeometry, laserMaterial);
    const rightLaser = new THREE.Mesh(laserGeometry, laserMaterial);

    // Create a single group to hold both lasers relative to the face
    const laserGroup = new THREE.Group(); 
    laserGroup.add(leftLaser);
    laserGroup.add(rightLaser);
    scene.add(laserGroup);

    return { leftLaser, rightLaser, laserGroup };
}

// 5. Main Animation and Detection Loop
async function animate() {
    // MediaPipe only needs to run detection if the video frame has advanced
    if (video.currentTime !== lastVideoTime && faceLandmarker) {
        lastVideoTime = video.currentTime;

        const results = faceLandmarker.detectForVideo(video, performance.now());

        if (results && results.faceLandmarks.length > 0) {
            const landmarks = results.faceLandmarks[0];
            const matrixData = results.facialTransformationMatrixes[0];

            if (matrixData) {
                // A. Apply Face Transformation Matrix (Rotation/Position)
                // This matrix transforms a canonical face mesh (centered at 0,0,0) 
                // to the real-time position/rotation/scale of the detected face.
                const matrix = new THREE.Matrix4().fromArray(matrixData.data);
                
                // Set the transformation matrix for the entire laser group
                lasers.laserGroup.matrixAutoUpdate = false;
                lasers.laserGroup.matrix.copy(matrix);

                // B. Position Lasers Relative to the Face Group
                // The landmarks (x,y,z) are now in a normalized world space based on the matrix.
                // We need to move them to their relative eye positions.
                
                const rightEyeLandmark = landmarks[RIGHT_EYE_LANDMARK_INDEX];
                const leftEyeLandmark = landmarks[LEFT_EYE_LANDMARK_INDEX];

                // The z coordinate is often inverted and needs scaling based on your scene size.
                // For the transformation matrix method, the z is usually correct relative to the face mesh.
                
                // Position Right Laser (relative to the face's center/pivot)
                lasers.rightLaser.position.set(
                    rightEyeLandmark.x,
                    -rightEyeLandmark.y, // Y-axis is often inverted between video and 3D
                    rightEyeLandmark.z
                );

                // Position Left Laser
                lasers.leftLaser.position.set(
                    leftEyeLandmark.x,
                    -leftEyeLandmark.y,
                    leftEyeLandmark.z
                );

                // C. Orient the Lasers
                // Since the matrix handles head rotation, the laser simply needs to point forward (along the Z-axis of the face).
                // The default cylinder geometry is oriented along the Y-axis. Rotate it to point forward (Z-axis).
                const rotationX = Math.PI / 2; // 90 degrees rotation to point from Y to Z

                lasers.rightLaser.rotation.x = rotationX;
                lasers.leftLaser.rotation.x = rotationX;
            }
        }
    }

    // Render the Three.js scene
    renderer.render(scene, camera);

    // Request the next frame
    requestAnimationFrame(animate);
}

// --- Main Execution ---
async function main() {
    try {
        await setupCamera();
        await setupFaceMesh();
        setupThreeJS();
        lasers = createLaserEffects();
        // Start the animation loop after everything is ready
        animate();
        console.log("AR application initialized. Looking for a face...");
    } catch (error) {
        console.error("Initialization failed:", error);
    }
}

main(); // Execute the main function when the module loads 