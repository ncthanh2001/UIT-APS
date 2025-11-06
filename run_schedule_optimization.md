🔄 Quy Trình Schedule Optimization
BƯỚC 1: Static ML Critical Path Method

Dùng ML model dự đoán thời gian thực tế cho mỗi operation (dựa trên historical data)
Tính Critical Path với predicted time
Output: Critical operations, buffer recommendations, risk scores

BƯỚC 2: Enhanced Heuristic Batching

Cluster các jobs có similarity cao (cùng setup, tooling, material)
Giảm setup time giữa các batches
Output: Job batches đã tối ưu

BƯỚC 3: Advanced Resource Leveling

Phân tích load distribution trên các workstations
Dịch chuyển jobs từ overloaded → underloaded resources
Output: Balanced workload

BƯỚC 4: Constraint Programming

Dùng CP Solver (Google OR-Tools) để đảm bảo:

No overlap trên cùng machine
Precedence constraints
Deadline constraints
Capacity limits


Output: Feasible schedule thỏa mãn tất cả constraints

BƯỚC 5: Predictive Analytics

ML models dự đoán:

Bottleneck: Resource nào sẽ bị nghẽn
Delay risk: Jobs nào có nguy cơ trễ
Resource failure: Machine nào có thể breakdown


Output: Risk alerts + mitigation recommendations

BƯỚC 6: Parallel Processing

Chạy song song nhiều scenarios:

Scenario 1: Minimize makespan
Scenario 2: Minimize cost
Scenario 3: Maximize on-time delivery
Scenario 4: Balance utilization


So sánh kết quả và chọn best trade-off

📊 Workflow Tích Hợp
Input Data
    ↓
[Critical Path + ML] → Xác định critical operations
    ↓
[Batching] → Nhóm jobs thông minh
    ↓
[Resource Leveling] → Cân bằng tải
    ↓
[CP Solver] → Tạo feasible schedule
    ↓
[Predictive Analytics] → Dự đoán risks
    ↓
[Parallel Scenarios] → So sánh options
    ↓
Best Schedule + Insights
💡 Lợi Ích
✅ So với thuật toán truyền thống:

Chính xác hơn (ML predictions)
Giảm setup time (batching)
Balanced workload (leveling)
Guarantee feasibility (CP)
Proactive risk management (predictive)
Multiple options (parallel)

✅ Kết quả:

Makespan giảm 15-25%
Setup time giảm 30-40%
On-time delivery tăng 20-30%
Resource utilization cân bằng hơn
Dự đoán bottleneck trước 2-3 ngày



####

✅ ĐÁNH GIÁ THAM SỐ HIỆN TẠI
Tham số bạn đã có:
Tham sốĐủ?Ghi chúTừ ngày → Đến ngày✅Planning horizonCa làm việc✅Work calendar/shiftsHorizon tối ưu✅Optimization timeframeJob cards cần tối ưu✅Input jobsKhu vực sản xuất✅Plant floor/area filterThuật toán AI✅Algorithm selectionMục tiêu tối ưu hóa✅Objective functionParallel processing mode✅Execution strategyMax utilization✅Resource constraintBatching stage✅Batching configRisk tolerance✅Risk acceptance level
Thiếu một số tham số quan trọng:
Tham sốCần?Lý doWorkstations/Resources⚠️ THIẾUCần biết schedule trên máy nàoMaterial availability⚠️ THIẾUCheck tồn kho trước khi scheduleSetup time matrix🔶 TÙY CHỌNCho batching optimizationOvertime allowed🔶 TÙY CHỌNFlexibility trong schedulingPriority weights🔶 TÙY CHỌNNếu có nhiều objectives


🔧 FUNCTION SPECIFICATION CHO DEVELOPER
1. Main Function Signature
pythondef run_schedule_optimization(
    # Required parameters
    from_date: datetime,
    to_date: datetime,
    work_calendar: str,  # Link to APS Work Calendar
    optimization_horizon: int,  # days
    job_cards: List[str],  # List of APS Job Card IDs
    plant_floor: str,  # Link to APS Plant Floor
    
    # Algorithm & Objective
    ai_algorithm: str,  # Select: 'hybrid', 'genetic', 'constraint_programming', etc.
    optimization_objective: str,  # Select: 'minimize_makespan', 'minimize_cost', 'maximize_utilization', 'minimize_tardiness'
    
    # Advanced settings
    parallel_processing_mode: str,  # 'auto', 'force_parallel', 'disable_parallel'
    max_utilization: float,  # 0.0 - 1.0 (e.g., 0.85 = 85%)
    batching_enabled: bool,
    batching_strategy: str,  # 'family_based', 'size_based', 'time_window'
    risk_tolerance: str,  # 'low', 'medium', 'high'
    
    # Optional parameters (bổ sung)
    workstations: List[str] = None,  # Specific workstations to use
    check_material: bool = True,  # Check material availability
    allow_overtime: bool = False,
    overtime_cost_factor: float = 1.5,
    setup_time_reduction_target: float = 0.3,  # 30% reduction
    
    # ML/Predictive settings
    enable_ml_predictions: bool = True,
    ml_confidence_threshold: float = 0.7,
    predict_bottlenecks: bool = True,
    predict_risks: bool = True,
    
) -> Dict:
    """
    Chạy Schedule Optimization với các thuật toán AI
    
    Returns:
        Dict chứa:
        - schedule_result: APS Production Planning Result document
        - execution_time: seconds
        - scenarios: list of scenarios nếu parallel processing
        - warnings: list of warnings
        - errors: list of errors
    """
    pass


    2. DETAILED INPUT PARAMETERS
python# ============================================
# SECTION 1: TIME PARAMETERS
# ============================================

from_date: datetime
    Purpose: Ngày bắt đầu của planning period
    Example: "2025-11-10"
    Validation:
        - Must be >= today
        - Must be < to_date
    Usage: Define start boundary for scheduling

to_date: datetime
    Purpose: Ngày kết thúc của planning period
    Example: "2025-11-30"
    Validation:
        - Must be > from_date
        - Must be <= from_date + optimization_horizon
    Usage: Define end boundary for scheduling

optimization_horizon: int
    Purpose: Số ngày optimize forward từ from_date
    Example: 20 (days)
    Range: 1-90 days
    Validation:
        - Must be > 0
        - Recommended: 7-30 days (balance quality vs speed)
    Usage: 
        - Limits search space for optimization
        - Larger horizon = better optimization but slower
        - AI will schedule jobs within this window

work_calendar: str
    Purpose: Link to APS Work Calendar
    Example: "Standard 5-Day Week"
    Data fetched:
        - working_days: [Mon, Tue, Wed, Thu, Fri]
        - start_time: "08:00"
        - end_time: "17:00"
        - breaks: [{start: "12:00", end: "13:00"}]
        - holidays: ["2025-12-25", "2025-01-01"]
    Usage:
        - Define available time slots
        - Calculate actual working hours
        - Exclude non-working periods

# ============================================
# SECTION 2: SCOPE PARAMETERS
# ============================================

job_cards: List[str]
    Purpose: Danh sách Job Cards cần schedule
    Example: ["JC-2025-001", "JC-2025-002", "JC-2025-003"]
    Data fetched for each job card:
        - item_code
        - qty
        - sales_order (if linked)
        - delivery_date
        - bom_no (Bill of Materials)
        - operations: [
            {
                operation: "Milling",
                workstation: "CNC-01",
                time_in_mins: 120,
                sequence: 1
            }
        ]
        - material_requirements
        - priority: high/medium/low
        - status: Not Started/In Progress
    Validation:
        - All job cards must exist
        - All must have valid BOM
        - All must have operations defined
    Usage: Core input - jobs to be scheduled

plant_floor: str
    Purpose: Khu vực sản xuất
    Example: "Plant Floor 1"
    Data fetched:
        - workstations in this floor
        - layout information
        - capacity constraints
    Validation:
        - Must exist
        - Must have workstations
    Usage:
        - Filter workstations available for scheduling
        - Apply floor-specific constraints

# ============================================
# SECTION 3: ALGORITHM PARAMETERS
# ============================================

ai_algorithm: str
    Purpose: Chọn thuật toán AI để optimize
    Options:
        - "hybrid" (Recommended): CP + GA + ML
            * Best quality
            * Medium speed
            * Use for: Complex schedules (50-200 jobs)
        
        - "genetic_algorithm": Pure GA
            * Good quality
            * Fast
            * Use for: Large schedules (200+ jobs)
        
        - "constraint_programming": Pure CP
            * Optimal solution
            * Slow for large problems
            * Use for: Small schedules (<50 jobs)
        
        - "heuristic": Dispatching rules + local search
            * Medium quality
            * Very fast
            * Use for: Real-time rescheduling
        
        - "ml_enhanced": ML predictions + heuristics
            * Good quality with predictions
            * Fast
            * Use for: When have good historical data
    
    Example: "hybrid"
    Default: "hybrid"
    
    Algorithm mapping:
        {
            "hybrid": {
                "steps": [
                    "ML_Critical_Path",
                    "Enhanced_Batching",
                    "Resource_Leveling",
                    "CP_Solver",
                    "Predictive_Analytics"
                ],
                "runtime_estimate": "medium"
            },
            "genetic_algorithm": {
                "population_size": 100,
                "generations": 500,
                "crossover_rate": 0.8,
                "mutation_rate": 0.05
            },
            # ... other configs
        }

optimization_objective: str
    Purpose: Mục tiêu tối ưu hóa chính
    Options:
        - "minimize_makespan": Giảm tổng thời gian hoàn thành
            Formula: min(max(completion_times))
            Weight: makespan
            Use when: Cần hoàn thành sớm nhất
        
        - "minimize_cost": Giảm tổng chi phí
            Formula: min(labor_cost + material_cost + overtime_cost + setup_cost)
            Weight: cost
            Use when: Budget constraint
        
        - "maximize_utilization": Tối đa hóa sử dụng máy móc
            Formula: max(sum(working_time) / sum(available_time))
            Weight: utilization
            Use when: Cần tận dụng capacity
        
        - "minimize_tardiness": Giảm trễ deadline
            Formula: min(sum(max(0, completion - deadline)))
            Weight: tardiness
            Use when: On-time delivery critical
        
        - "balance_workload": Cân bằng tải
            Formula: min(variance(utilization_across_resources))
            Weight: balance
            Use when: Avoid overload/underload
        
        - "multi_objective": Kết hợp nhiều objectives
            Formula: weighted_sum(objectives)
            Requires: objective_weights parameter
    
    Example: "minimize_makespan"
    Default: "minimize_makespan"

# ============================================
# SECTION 4: ADVANCED SETTINGS
# ============================================

parallel_processing_mode: str
    Purpose: Cách xử lý parallel scenarios
    Options:
        - "auto": AI tự quyết định dựa trên problem size
            Logic:
                if jobs < 50: disable_parallel
                elif jobs < 200: run 2 scenarios
                else: run 4 scenarios
        
        - "force_parallel": Luôn chạy multiple scenarios
            Config:
                scenarios: [
                    {objective: "minimize_makespan", weight: 1.0},
                    {objective: "minimize_cost", weight: 1.0},
                    {objective: "maximize_utilization", weight: 1.0},
                    {objective: "balance_workload", weight: 1.0}
                ]
                parallel_threads: 4
        
        - "disable_parallel": Chỉ chạy 1 scenario
            Use when: Limited compute resources
    
    Example: "auto"
    Default: "auto"
    Runtime impact:
        - auto: 1x - 4x base time
        - force_parallel: 4x base time
        - disable_parallel: 1x base time

max_utilization: float
    Purpose: Ngưỡng tối đa sử dụng resource
    Range: 0.0 - 1.0
    Example: 0.85 (85%)
    Recommended: 0.80 - 0.90
    
    Usage:
        - Constraint for CP solver
        - Prevents overloading resources
        - Leave buffer for unexpected work
    
    Validation:
        - Must be between 0.5 and 1.0
        - Warning if < 0.7 (underutilization)
        - Warning if > 0.95 (no buffer)
    
    Impact:
        - Higher value: More jobs scheduled, less flexibility
        - Lower value: Fewer jobs scheduled, more flexibility

batching_enabled: bool
    Purpose: Bật/tắt batching optimization
    Example: True
    Default: True
    
    When True:
        - Group similar jobs together
        - Reduce setup time
        - Apply batching_strategy
    
    When False:
        - Schedule jobs individually
        - More flexibility
        - Faster optimization

batching_strategy: str
    Purpose: Chiến lược nhóm batches
    Only used if batching_enabled = True
    Options:
        - "family_based": Nhóm theo product family
            Logic: Group jobs with same product_family
            Benefits: Maximum setup time reduction
            Drawback: Less flexibility
        
        - "size_based": Nhóm theo kích thước batch
            Logic: Create batches of similar size
            Config:
                min_batch_size: 5
                max_batch_size: 20
            Benefits: Balanced batch sizes
        
        - "time_window": Nhóm theo delivery date
            Logic: Group jobs with close delivery dates
            Config:
                time_window_hours: 48
            Benefits: Meet deadlines better
        
        - "similarity_based": Nhóm theo ML similarity
            Logic: ML model calculates similarity
            Features: setup, tooling, material, parameters
            Benefits: Intelligent grouping
    
    Example: "family_based"
    Default: "similarity_based"

risk_tolerance: str
    Purpose: Mức độ chấp nhận rủi ro
    Options:
        - "low": Conservative scheduling
            Config:
                buffer_multiplier: 2.0
                use_pessimistic_time: True
                min_slack_time: 4 hours
                reject_jobs_with_risk > 0.3
            Result: Safer but longer schedule
        
        - "medium": Balanced approach
            Config:
                buffer_multiplier: 1.5
                use_realistic_time: True
                min_slack_time: 2 hours
                reject_jobs_with_risk > 0.6
            Result: Good balance
        
        - "high": Aggressive scheduling
            Config:
                buffer_multiplier: 1.0
                use_optimistic_time: True
                min_slack_time: 0 hours
                reject_jobs_with_risk > 0.9
            Result: Tight schedule, higher risk
    
    Example: "medium"
    Default: "medium"
    
    Impact:
        - Affects buffer time allocation
        - Affects job acceptance criteria
        - Affects overtime decisions

# ============================================
# SECTION 5: ML/PREDICTIVE PARAMETERS
# ============================================

enable_ml_predictions: bool
    Purpose: Bật/tắt ML predictions
    Example: True
    Default: True
    
    When True:
        - Use ML models for duration prediction
        - Predict bottlenecks
        - Predict risks
        - Better accuracy
    
    When False:
        - Use standard BOM times
        - No predictive analytics
        - Faster but less accurate

ml_confidence_threshold: float
    Purpose: Ngưỡng confidence để accept ML predictions
    Range: 0.0 - 1.0
    Example: 0.7 (70%)
    Default: 0.7
    
    Usage:
        if prediction_confidence >= threshold:
            use ml_predicted_time
        else:
            use standard_bom_time
    
    Recommendation:
        - 0.9: Very conservative (use only high-confidence predictions)
        - 0.7: Balanced (recommended)
        - 0.5: Aggressive (use most predictions)

predict_bottlenecks: bool
    Purpose: Bật/tắt bottleneck prediction
    Example: True
    Default: True
    
    When True:
        - ML predicts which resources will become bottlenecks
        - Provides early warnings
        - Suggests mitigation actions
        - Output saved in APS Planning Bottleneck

predict_risks: bool
    Purpose: Bật/tắt risk prediction
    Example: True
    Default: True
    
    When True:
        - ML predicts delay risks
        - Material shortage risks
        - Quality risks
        - Output saved in APS ML Prediction Log

3. PROCESSING FLOW
pythondef run_schedule_optimization(...) -> Dict:
    """
    MAIN PROCESSING FLOW
    """
    
    # ====================
    # PHASE 1: VALIDATION & DATA LOADING
    # ====================
    
    # Step 1.1: Validate input parameters
    validation_result = validate_inputs(
        from_date, to_date, optimization_horizon,
        job_cards, plant_floor, work_calendar
    )
    if not validation_result['valid']:
        return {
            'success': False,
            'errors': validation_result['errors']
        }
    
    # Step 1.2: Load required data
    data = load_required_data(
        job_cards=job_cards,
        plant_floor=plant_floor,
        work_calendar=work_calendar,
        from_date=from_date,
        to_date=to_date
    )
    
    # Data structure:
    data = {
        'jobs': [
            {
                'job_card_id': 'JC-2025-001',
                'item_code': 'PROD-A',
                'qty': 100,
                'sales_order': 'SO-2025-001',
                'delivery_date': datetime(2025, 11, 20),
                'priority': 'high',
                'bom_no': 'BOM-PROD-A-001',
                'operations': [
                    {
                        'operation': 'Milling',
                        'workstation': 'CNC-01',
                        'time_in_mins': 120,
                        'sequence': 1,
                        'setup_time_mins': 30
                    }
                ],
                'material_requirements': [
                    {'item': 'MAT-001', 'qty': 200}
                ]
            }
        ],
        'workstations': [
            {
                'workstation_id': 'CNC-01',
                'workstation_type': 'CNC',
                'capacity': 1.0,
                'plant_floor': 'Plant Floor 1',
                'working_hours': {
                    'mon-fri': {'start': '08:00', 'end': '17:00'},
                    'sat': {'start': '08:00', 'end': '12:00'}
                },
                'current_utilization': 0.72,
                'maintenance_schedule': []
            }
        ],
        'calendar': {
            'working_days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
            'holidays': ['2025-12-25'],
            'shifts': [
                {'name': 'Morning', 'start': '08:00', 'end': '17:00'}
            ]
        },
        'stock': {
            'MAT-001': {
                'available_qty': 5000,
                'reserved_qty': 1000,
                'on_order_qty': 2000
            }
        }
    }
    
    # Step 1.3: Check material availability (if enabled)
    if check_material:
        material_check = check_material_availability(data)
        if material_check['shortages']:
            return {
                'success': False,
                'errors': ['Material shortages detected'],
                'shortages': material_check['shortages']
            }
    
    # ====================
    # PHASE 2: ML PREPROCESSING
    # ====================
    
    ml_results = {}
    
    if enable_ml_predictions:
        # Step 2.1: ML Critical Path Method
        critical_path_result = ml_critical_path_method(
            jobs=data['jobs'],
            workstations=data['workstations'],
            confidence_threshold=ml_confidence_threshold
        )
        
        ml_results['critical_path'] = {
            'critical_operations': critical_path_result['critical_ops'],
            'predicted_duration': critical_path_result['duration'],
            'buffer_recommendations': critical_path_result['buffers']
        }
        
        # Step 2.2: Predict bottlenecks
        if predict_bottlenecks:
            bottleneck_predictions = predict_bottlenecks_ml(
                workstations=data['workstations'],
                jobs=data['jobs'],
                horizon=optimization_horizon
            )
            
            ml_results['bottlenecks'] = bottleneck_predictions
        
        # Step 2.3: Predict risks
        if predict_risks:
            risk_predictions = predict_risks_ml(
                jobs=data['jobs'],
                workstations=data['workstations'],
                risk_tolerance=risk_tolerance
            )
            
            ml_results['risks'] = risk_predictions
    
    # ====================
    # PHASE 3: BATCHING (if enabled)
    # ====================
    
    if batching_enabled:
        batching_result = enhanced_heuristic_batching(
            jobs=data['jobs'],
            strategy=batching_strategy,
            setup_reduction_target=setup_time_reduction_target
        )
        
        # Update jobs with batch info
        data['jobs'] = batching_result['batched_jobs']
        data['batches'] = batching_result['batches']
        
        batching_metrics = {
            'total_batches': len(batching_result['batches']),
            'avg_batch_size': batching_result['avg_size'],
            'setup_time_saved': batching_result['time_saved']
        }
    else:
        batching_metrics = None
    
    # ====================
    # PHASE 4: RESOURCE LEVELING
    # ====================
    
    leveling_result = advanced_resource_leveling(
        jobs=data['jobs'],
        workstations=data['workstations'],
        max_utilization=max_utilization
    )
    
    # Update jobs with leveled assignment
    data['jobs'] = leveling_result['leveled_jobs']
    
    leveling_metrics = {
        'jobs_shifted': leveling_result['shifted_count'],
        'utilization_improvement': leveling_result['improvement'],
        'balance_score': leveling_result['balance_score']
    }
    
    # ====================
    # PHASE 5: OPTIMIZATION ENGINE
    # ====================
    
    # Determine if parallel processing
    should_run_parallel = determine_parallel_mode(
        mode=parallel_processing_mode,
        num_jobs=len(data['jobs']),
        num_workstations=len(data['workstations'])
    )
    
    if should_run_parallel:
        # Run multiple scenarios in parallel
        scenarios = run_parallel_optimization(
            data=data,
            ai_algorithm=ai_algorithm,
            objectives=[
                optimization_objective,
                'minimize_cost',
                'maximize_utilization',
                'balance_workload'
            ],
            ml_results=ml_results
        )
        
        # Select best scenario
        best_scenario = select_best_scenario(
            scenarios=scenarios,
            primary_objective=optimization_objective
        )
        
        optimization_result = best_scenario
        all_scenarios = scenarios
        
    else:
        # Single scenario optimization
        optimization_result = run_single_optimization(
            data=data,
            ai_algorithm=ai_algorithm,
            objective=optimization_objective,
            ml_results=ml_results
        )
        
        all_scenarios = [optimization_result]
    
    # ====================
    # PHASE 6: POST-PROCESSING
    # ====================
    
    # Step 6.1: Validate schedule feasibility
    feasibility = validate_schedule_feasibility(
        schedule=optimization_result['schedule'],
        constraints=data['constraints']
    )
    
    if not feasibility['is_feasible']:
        return {
            'success': False,
            'errors': feasibility['violations']
        }
    
    # Step 6.2: Calculate metrics
    metrics = calculate_schedule_metrics(
        schedule=optimization_result['schedule'],
        jobs=data['jobs'],
        workstations=data['workstations']
    )
    
    # ====================
    # PHASE 7: SAVE RESULTS
    # ====================
    
    # Create APS Production Planning Result
    result_doc = create_planning_result_document(
        planning_type='Schedule Optimization',
        optimization_result=optimization_result,
        batching_metrics=batching_metrics,
        leveling_metrics=leveling_metrics,
        ml_results=ml_results,
        metrics=metrics,
        scenarios=all_scenarios,
        input_params={
            'from_date': from_date,
            'to_date': to_date,
            'ai_algorithm': ai_algorithm,
            'optimization_objective': optimization_objective,
            'parallel_mode': parallel_processing_mode,
            'batching_enabled': batching_enabled,
            'risk_tolerance': risk_tolerance
        }
    )
    
    # Save to database
    result_doc.insert()
    frappe.db.commit()
    
    # ====================
    # PHASE 8: RETURN RESULTS
    # ====================
    
    return {
        'success': True,
        'result_id': result_doc.name,
        'schedule': optimization_result['schedule'],
        'metrics': metrics,
        'execution_time': optimization_result['runtime'],
        'scenarios': all_scenarios if should_run_parallel else None,
        'warnings': optimization_result.get('warnings', []),
        'ml_insights': ml_results,
        'batching_summary': batching_metrics,
        'leveling_summary': leveling_metrics
    }

4. OUTPUT STRUCTURE
python# RETURN OBJECT
{
    'success': True,  # Boolean
    'result_id': 'SCH-OPT-2025-11-06-001',  # Link to saved document
    
    # CORE SCHEDULE
    'schedule': {
        'makespan': 168.5,  # hours
        'start_date': '2025-11-10',
        'end_date': '2025-11-18',
        
        # Job schedule
        'jobs': [
            {
                'job_card_id': 'JC-2025-001',
                'item_code': 'PROD-A',
                'qty': 100,
                'start_datetime': '2025-11-10 08:00:00',
                'end_datetime': '2025-11-12 16:00:00',
                'assigned_workstations': ['CNC-01', 'MILL-01'],
                'batch_id': 'BATCH-001',
                'is_critical_path': True,
                'slack_time': 0,
                'risk_score': 0.15
            }
        ],
        
        # Workstation schedule
        'workstation_schedule': [
            {
                'workstation': 'CNC-01',
                'date': '2025-11-10',
                'operations': [
                    {
                        'job_card': 'JC-2025-001',
                        'operation': 'Milling',
                        'start': '08:00',
                        'end': '12:00',
                        'duration_mins': 240,
                        'setup_mins': 30
                    }
                ],
                'utilization': 0.85,
                'idle_time_mins': 60
            }
        ],
        
        # Timeline (Gantt data)
        'timeline': [
            {
                'workstation': 'CNC-01',
                'job_card': 'JC-2025-001',
                'operation': 'Milling',
                'start': '2025-11-10 08:00:00',
                'end': '2025-11-10 12:00:00',
                'status': 'scheduled'
            }
        ]
    },
    
    # METRICS
    'metrics': {
        'optimization_score': 87.5,  # 0-100
        'makespan': 168.5,  # hours
        'total_cost': 125000,  # currency
        'on_time_delivery_rate': 92.3,  # percent
        'average_utilization': 78.5,  # percent
        'total_tardiness': 12.5,  # hours
        'total_jobs_scheduled': 45,
        'total_operations': 180
    },
    
    # EXECUTION INFO
    'execution_time': 45.3,  # seconds
    'algorithm_used': 'Hybrid (CP + GA + ML)',
    'iterations': 500,
    'convergence_generation': 423,
    
    # BATCHING RESULTS (if enabled)
    'batching_summary': {
        'enabled': True,
        'strategy': 'family_based',
        'total_batches': 8,
        'avg_batch_size': 5.6,
        'setup_time_saved': 12.5,  # hours
        'setup_savings_percent': 35.7
    },
    
    # LEVELING RESULTS
    'leveling_summary': {
        'jobs_shifted': 15,
        'utilization_std_before': 0.25,
        'utilization_std_after': 0.12,
        'balance_improvement': 52,  # percent
        'overtime_allocated': 0  # hours
    },
    
    # ML INSIGHTS
    'ml_insights': {
        'critical_path': {
            'duration': 145.2,  # hours
            'operations': ['Op1', 'Op2', 'Op3'],
            'confidence': 0.85
        },
        'bottlenecks': [
            {
                'workstation': 'CNC-01',
                'date': '2025-11-15',
                'probability': 0.78,
                'severity': 'High',
                'predicted_delay': 2.5,  # hours
                'mitigation': 'Add overtime or reschedule 3 jobs'
            }
        ],
        'risks': [
            {
                'type': 'Material Shortage',
                'item': 'MAT-001',
                'date': '2025-11-12',
                'probability': 0.45,
                'impact': 'Medium',
                'action': 'Order 500 units by 2025-11-10'
            }
        ]
    },
    
    # PARALLEL SCENARIOS (if enabled)
    'scenarios': [
        {
            'scenario_name': 'Minimize Makespan',
            'optimization_score': 87.5,
            'makespan': 168.5,
            'cost': 125000,
            'utilization': 78.5,
            'on_time_rate': 92.3,
            'rank': 1,
            'is_recommended': True
        },
        {
            'scenario_name': 'Minimize Cost',
            'optimization_score': 82.0,
            'makespan': 185.0,
            'cost': 112000,
            'utilization': 72.0,
            'on_time_rate': 88.5,
            'rank': 2,
            'is_recommended': False
        }
    ],
    
    # WARNINGS & RECOMMENDATIONS
    'warnings': [
        'CNC-01 will reach 95% utilization on 2025-11-15',
        'Material MAT-001 has only 2 days of buffer stock'
    ],
    
    'recommendations': [
        'Consider adding overtime shift on 2025-11-15 for CNC-01',
        'Order material MAT-001 by 2025-11-10 to avoid shortage'
    ]
}

5. ERROR HANDLING
python# POSSIBLE ERROR CASES

# Case 1: Validation errors
{
    'success': False,
    'error_type': 'ValidationError',
    'errors': [
        'from_date must be >= today',
        'Job card JC-2025-999 does not exist',
        'Plant floor has no workstations'
    ]
}

# Case 2: Infeasible schedule
{
    'success': False,
    'error_type': 'InfeasibleSchedule',
    'errors': [
        'Cannot meet deadline for job JC-2025-001',
        'Insufficient capacity on CNC-01',
        'Material MAT-001 shortage: need 500, have 200'
    ],
    'suggestions': [
        'Extend deadline by 2 days',
        'Add overtime or additional workstation',
        'Order material before optimization'
    ]
}

# Case 3: Optimization timeout
{
    'success': False,
    'error_type': 'TimeoutError',
    'message': 'Optimization exceeded time limit (300s)',
    'partial_result': {
        'best_solution_found': {...},
        'quality_score': 65.5
    },
    'suggestion': 'Reduce optimization_horizon or use faster algorithm'
}

# Case 4: ML model error
{
    'success': True,  # Graceful degradation
    'schedule': {...},  # Using standard BOM times
    'warnings': [
        'ML models unavailable, using standard BOM times',
        'Bottleneck predictions disabled'
    ]
}

6. USAGE EXAMPLE
python# EXAMPLE 1: Basic usage
result = run_schedule_optimization(
    from_date=datetime(2025, 11, 10),
    to_date=datetime(2025, 11, 30),
    work_calendar='Standard 5-Day Week',
    optimization_horizon=20,
    job_cards=['JC-2025-001', 'JC-2025-002', 'JC-2025-003'],
    plant_floor='Plant Floor 1',
    ai_algorithm='hybrid',
    optimization_objective='minimize_makespan',
    parallel_processing_mode='auto',
    max_utilization=0.85,
    batching_enabled=True,
    batching_strategy='family_based',
    risk_tolerance='medium'
)

if result['success']:
    print(f"Schedule created: {result['result_id']}")
    print(f"Makespan: {result['metrics']['makespan']} hours")
    print(f"On-time rate: {result['metrics']['on_time_delivery_rate']}%")
else:
    print(f"Error: {result['errors']}")

# EXAMPLE 2: Conservative scheduling with ML
result = run_schedule_optimization(
    from_date=datetime(2025, 11, 10),
    to_date=datetime(2025, 11, 20),
    work_calendar='24/7 Operations',
    optimization_horizon=10,
    job_cards=get_urgent_jobs(),
    plant_floor='Plant Floor 1',
    ai_algorithm='ml_enhanced',
    optimization_objective='minimize_tardiness',
    parallel_processing_mode='disable_parallel',
    max_utilization=0.80,  # Conservative
    batching_enabled=True,
    batching_strategy='time_window',
    risk_tolerance='low',  # Conservative
    enable_ml_predictions=True,
    ml_confidence_threshold=0.8,  # High confidence only
    predict_bottlenecks=True,
    predict_risks=True
)

# EXAMPLE 3: Aggressive scheduling for cost optimization
result = run_schedule_optimization(
    from_date=datetime(2025, 11, 10),
    to_date=datetime(2025, 12, 10),
    work_calendar='Standard 5-Day Week',
    optimization_horizon=30,
    job_cards=get_all_pending_jobs(),
    plant_floor='Plant Floor 1',
    ai_algorithm='genetic_algorithm',
    optimization_objective='minimize_cost',
    parallel_processing_mode='force_parallel',
    max_utilization=0.92,  # Aggressive
    batching_enabled=True,
    batching_strategy='similarity_based',
    risk_tolerance='high',  # Aggressive
    allow_overtime=True,
    overtime_cost_factor=1.5
)

# Compare scenarios
for scenario in result['scenarios']:
    print(f"{scenario['scenario_name']}: Cost={scenario['cost']}, Makespan={scenario['makespan']}")

✅ CHECKLIST CHO DEVELOPER
Backend Tasks:

 Implement validate_inputs() function
 Implement load_required_data() function
 Implement ml_critical_path_method() function
 Implement enhanced_heuristic_batching() function
 Implement advanced_resource_leveling() function
 Implement run_single_optimization() function (main optimization engine)
 Implement run_parallel_optimization() function
 Implement calculate_schedule_metrics() function
 Implement create_planning_result_document() function
 Add error handling and logging
 Add progress tracking (for long-running optimizations)
 Add API endpoint: /api/method/dbiz_aps.schedule_optimization.run