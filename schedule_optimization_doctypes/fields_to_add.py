# FIELDS TO ADD TO EXISTING DOCTYPES
# Schedule Optimization Enhancement
# Date: 2025-11-06

"""
Instructions:
1. Open each DocType in Frappe
2. Click "Customize Form"
3. Add fields as listed below
4. Save and Reload
"""

## ===========================================
## APS PRODUCTION PLANNING RESULT
## Add these fields
## ===========================================

APS_PRODUCTION_PLANNING_RESULT_FIELDS = [
    # Section: Schedule Optimization Settings
    {
        "fieldname": "schedule_optimization_section",
        "fieldtype": "Section Break",
        "label": "Schedule Optimization",
        "collapsible": 1,
        "depends_on": "eval:doc.planning_type=='Schedule Optimization'",
        "insert_after": "planning_type"  # Adjust based on your existing fields
    },
    
    # Algorithm Info
    {
        "fieldname": "ai_algorithm_used",
        "fieldtype": "Data",
        "label": "AI Algorithm Used",
        "insert_after": "schedule_optimization_section"
    },
    {
        "fieldname": "optimization_objective",
        "fieldtype": "Select",
        "label": "Optimization Objective",
        "options": "Minimize Makespan\nMinimize Cost\nMaximize Utilization\nMinimize Tardiness\nBalance Workload\nMulti-Objective",
        "insert_after": "ai_algorithm_used"
    },
    {
        "fieldname": "optimization_horizon_days",
        "fieldtype": "Int",
        "label": "Optimization Horizon (Days)",
        "insert_after": "optimization_objective"
    },
    
    # Column Break
    {
        "fieldname": "column_break_opt_1",
        "fieldtype": "Column Break",
        "insert_after": "optimization_horizon_days"
    },
    
    {
        "fieldname": "optimization_runtime_seconds",
        "fieldtype": "Float",
        "label": "Optimization Runtime (Seconds)",
        "read_only": 1,
        "insert_after": "column_break_opt_1"
    },
    {
        "fieldname": "iterations_completed",
        "fieldtype": "Int",
        "label": "Iterations Completed",
        "read_only": 1,
        "insert_after": "optimization_runtime_seconds"
    },
    {
        "fieldname": "convergence_iteration",
        "fieldtype": "Int",
        "label": "Convergence Iteration",
        "read_only": 1,
        "insert_after": "iterations_completed"
    },
    
    # Critical Path Section
    {
        "fieldname": "critical_path_section",
        "fieldtype": "Section Break",
        "label": "Critical Path Analysis",
        "collapsible": 1,
        "depends_on": "eval:doc.planning_type=='Schedule Optimization'",
        "insert_after": "convergence_iteration"
    },
    {
        "fieldname": "critical_path_identified",
        "fieldtype": "Check",
        "label": "Critical Path Identified",
        "insert_after": "critical_path_section"
    },
    {
        "fieldname": "critical_path_duration_hours",
        "fieldtype": "Float",
        "label": "Critical Path Duration (Hours)",
        "insert_after": "critical_path_identified"
    },
    {
        "fieldname": "critical_path_operations",
        "fieldtype": "Long Text",
        "label": "Critical Path Operations (JSON)",
        "insert_after": "critical_path_duration_hours"
    },
    {
        "fieldname": "column_break_cp_1",
        "fieldtype": "Column Break",
        "insert_after": "critical_path_operations"
    },
    {
        "fieldname": "total_buffer_time_hours",
        "fieldtype": "Float",
        "label": "Total Buffer Time (Hours)",
        "insert_after": "column_break_cp_1"
    },
    
    # Batching Section
    {
        "fieldname": "batching_section",
        "fieldtype": "Section Break",
        "label": "Batching",
        "collapsible": 1,
        "depends_on": "eval:doc.planning_type=='Schedule Optimization'",
        "insert_after": "total_buffer_time_hours"
    },
    {
        "fieldname": "batching_enabled",
        "fieldtype": "Check",
        "label": "Batching Enabled",
        "insert_after": "batching_section"
    },
    {
        "fieldname": "batching_strategy",
        "fieldtype": "Data",
        "label": "Batching Strategy",
        "depends_on": "eval:doc.batching_enabled==1",
        "insert_after": "batching_enabled"
    },
    {
        "fieldname": "total_batches",
        "fieldtype": "Int",
        "label": "Total Batches",
        "read_only": 1,
        "depends_on": "eval:doc.batching_enabled==1",
        "insert_after": "batching_strategy"
    },
    {
        "fieldname": "column_break_batch_1",
        "fieldtype": "Column Break",
        "insert_after": "total_batches"
    },
    {
        "fieldname": "average_batch_size",
        "fieldtype": "Float",
        "label": "Average Batch Size",
        "read_only": 1,
        "depends_on": "eval:doc.batching_enabled==1",
        "insert_after": "column_break_batch_1"
    },
    {
        "fieldname": "setup_time_saved_hours",
        "fieldtype": "Float",
        "label": "Setup Time Saved (Hours)",
        "read_only": 1,
        "depends_on": "eval:doc.batching_enabled==1",
        "insert_after": "average_batch_size"
    },
    {
        "fieldname": "setup_savings_percent",
        "fieldtype": "Percent",
        "label": "Setup Savings (%)",
        "read_only": 1,
        "depends_on": "eval:doc.batching_enabled==1",
        "insert_after": "setup_time_saved_hours"
    },
    
    # Resource Leveling Section
    {
        "fieldname": "leveling_section",
        "fieldtype": "Section Break",
        "label": "Resource Leveling",
        "collapsible": 1,
        "depends_on": "eval:doc.planning_type=='Schedule Optimization'",
        "insert_after": "setup_savings_percent"
    },
    {
        "fieldname": "leveling_applied",
        "fieldtype": "Check",
        "label": "Leveling Applied",
        "insert_after": "leveling_section"
    },
    {
        "fieldname": "utilization_std_before",
        "fieldtype": "Float",
        "label": "Utilization Std Before",
        "precision": 4,
        "depends_on": "eval:doc.leveling_applied==1",
        "insert_after": "leveling_applied"
    },
    {
        "fieldname": "utilization_std_after",
        "fieldtype": "Float",
        "label": "Utilization Std After",
        "precision": 4,
        "depends_on": "eval:doc.leveling_applied==1",
        "insert_after": "utilization_std_before"
    },
    {
        "fieldname": "column_break_level_1",
        "fieldtype": "Column Break",
        "insert_after": "utilization_std_after"
    },
    {
        "fieldname": "balance_improvement_percent",
        "fieldtype": "Percent",
        "label": "Balance Improvement (%)",
        "read_only": 1,
        "depends_on": "eval:doc.leveling_applied==1",
        "insert_after": "column_break_level_1"
    },
    {
        "fieldname": "jobs_shifted_count",
        "fieldtype": "Int",
        "label": "Jobs Shifted",
        "read_only": 1,
        "depends_on": "eval:doc.leveling_applied==1",
        "insert_after": "balance_improvement_percent"
    },
    {
        "fieldname": "overtime_allocated_hours",
        "fieldtype": "Float",
        "label": "Overtime Allocated (Hours)",
        "depends_on": "eval:doc.leveling_applied==1",
        "insert_after": "jobs_shifted_count"
    },
    
    # Constraint Programming Section
    {
        "fieldname": "cp_section",
        "fieldtype": "Section Break",
        "label": "Constraint Programming",
        "collapsible": 1,
        "depends_on": "eval:doc.planning_type=='Schedule Optimization'",
        "insert_after": "overtime_allocated_hours"
    },
    {
        "fieldname": "cp_solver_used",
        "fieldtype": "Data",
        "label": "CP Solver Used",
        "insert_after": "cp_section"
    },
    {
        "fieldname": "cp_solver_status",
        "fieldtype": "Select",
        "label": "CP Solver Status",
        "options": "Optimal\nFeasible\nInfeasible\nTimeout",
        "insert_after": "cp_solver_used"
    },
    {
        "fieldname": "cp_runtime_seconds",
        "fieldtype": "Float",
        "label": "CP Runtime (Seconds)",
        "insert_after": "cp_solver_status"
    },
    {
        "fieldname": "column_break_cp_1",
        "fieldtype": "Column Break",
        "insert_after": "cp_runtime_seconds"
    },
    {
        "fieldname": "constraints_total",
        "fieldtype": "Int",
        "label": "Total Constraints",
        "insert_after": "column_break_cp_1"
    },
    {
        "fieldname": "constraints_satisfied",
        "fieldtype": "Int",
        "label": "Constraints Satisfied",
        "insert_after": "constraints_total"
    },
    {
        "fieldname": "constraints_violated",
        "fieldtype": "Int",
        "label": "Constraints Violated",
        "insert_after": "constraints_satisfied"
    },
    
    # ML Predictions Section
    {
        "fieldname": "ml_section",
        "fieldtype": "Section Break",
        "label": "ML Predictions",
        "collapsible": 1,
        "depends_on": "eval:doc.planning_type=='Schedule Optimization'",
        "insert_after": "constraints_violated"
    },
    {
        "fieldname": "ml_enabled",
        "fieldtype": "Check",
        "label": "ML Enabled",
        "insert_after": "ml_section"
    },
    {
        "fieldname": "ml_models_used",
        "fieldtype": "Small Text",
        "label": "ML Models Used",
        "depends_on": "eval:doc.ml_enabled==1",
        "insert_after": "ml_enabled"
    },
    {
        "fieldname": "ml_confidence_level",
        "fieldtype": "Percent",
        "label": "ML Confidence Level",
        "depends_on": "eval:doc.ml_enabled==1",
        "insert_after": "ml_models_used"
    },
    {
        "fieldname": "column_break_ml_1",
        "fieldtype": "Column Break",
        "insert_after": "ml_confidence_level"
    },
    {
        "fieldname": "bottlenecks_predicted",
        "fieldtype": "Int",
        "label": "Bottlenecks Predicted",
        "depends_on": "eval:doc.ml_enabled==1",
        "insert_after": "column_break_ml_1"
    },
    {
        "fieldname": "high_risk_operations",
        "fieldtype": "Int",
        "label": "High Risk Operations",
        "depends_on": "eval:doc.ml_enabled==1",
        "insert_after": "bottlenecks_predicted"
    },
    {
        "fieldname": "ml_prediction_accuracy",
        "fieldtype": "Percent",
        "label": "ML Prediction Accuracy",
        "description": "Filled after actual execution",
        "depends_on": "eval:doc.ml_enabled==1",
        "insert_after": "high_risk_operations"
    },
    
    # Parallel Processing Section
    {
        "fieldname": "parallel_section",
        "fieldtype": "Section Break",
        "label": "Parallel Processing",
        "collapsible": 1,
        "depends_on": "eval:doc.planning_type=='Schedule Optimization'",
        "insert_after": "ml_prediction_accuracy"
    },
    {
        "fieldname": "parallel_mode",
        "fieldtype": "Select",
        "label": "Parallel Mode",
        "options": "Single\nParallel",
        "insert_after": "parallel_section"
    },
    {
        "fieldname": "scenarios_generated",
        "fieldtype": "Int",
        "label": "Scenarios Generated",
        "depends_on": "eval:doc.parallel_mode=='Parallel'",
        "insert_after": "parallel_mode"
    },
    {
        "fieldname": "column_break_par_1",
        "fieldtype": "Column Break",
        "insert_after": "scenarios_generated"
    },
    {
        "fieldname": "is_recommended_scenario",
        "fieldtype": "Check",
        "label": "Recommended Scenario",
        "depends_on": "eval:doc.parallel_mode=='Parallel'",
        "insert_after": "column_break_par_1"
    },
    {
        "fieldname": "scenario_comparison",
        "fieldtype": "Link",
        "label": "Scenario Comparison",
        "options": "APS Scenario Comparison",
        "depends_on": "eval:doc.parallel_mode=='Parallel'",
        "insert_after": "is_recommended_scenario"
    },
    
    # Links Section
    {
        "fieldname": "links_section",
        "fieldtype": "Section Break",
        "label": "Related Documents",
        "collapsible": 1,
        "depends_on": "eval:doc.planning_type=='Schedule Optimization'",
        "insert_after": "scenario_comparison"
    },
    {
        "fieldname": "optimization_log",
        "fieldtype": "Link",
        "label": "Optimization Log",
        "options": "APS Optimization Run Log",
        "insert_after": "links_section"
    },
    {
        "fieldname": "batch_schedules",
        "fieldtype": "Long Text",
        "label": "Batch Schedules (JSON)",
        "description": "Links to batch schedule documents",
        "insert_after": "optimization_log"
    }
]

## ===========================================
## APS PRODUCTION PLANNING ITEM RESULT
## Add these fields
## ===========================================

APS_PRODUCTION_PLANNING_ITEM_RESULT_FIELDS = [
    # Batching Fields
    {
        "fieldname": "batch_id",
        "fieldtype": "Data",
        "label": "Batch ID",
        "in_list_view": 0,
        "insert_after": "item_code"  # Adjust based on existing fields
    },
    {
        "fieldname": "batch_sequence",
        "fieldtype": "Int",
        "label": "Batch Sequence",
        "insert_after": "batch_id"
    },
    {
        "fieldname": "setup_time_mins",
        "fieldtype": "Float",
        "label": "Setup Time (Mins)",
        "insert_after": "batch_sequence"
    },
    {
        "fieldname": "similarity_to_previous",
        "fieldtype": "Percent",
        "label": "Similarity to Previous",
        "insert_after": "setup_time_mins"
    },
    
    # Critical Path Fields
    {
        "fieldname": "is_critical_path",
        "fieldtype": "Check",
        "label": "Critical Path",
        "in_list_view": 1,
        "insert_after": "similarity_to_previous"
    },
    {
        "fieldname": "slack_time_hours",
        "fieldtype": "Float",
        "label": "Slack Time (Hours)",
        "insert_after": "is_critical_path"
    },
    {
        "fieldname": "early_start",
        "fieldtype": "Datetime",
        "label": "Early Start",
        "insert_after": "slack_time_hours"
    },
    {
        "fieldname": "early_finish",
        "fieldtype": "Datetime",
        "label": "Early Finish",
        "insert_after": "early_start"
    },
    {
        "fieldname": "late_start",
        "fieldtype": "Datetime",
        "label": "Late Start",
        "insert_after": "early_finish"
    },
    {
        "fieldname": "late_finish",
        "fieldtype": "Datetime",
        "label": "Late Finish",
        "insert_after": "late_start"
    },
    
    # Risk Assessment Fields
    {
        "fieldname": "risk_score",
        "fieldtype": "Percent",
        "label": "Risk Score",
        "insert_after": "late_finish"
    },
    {
        "fieldname": "risk_type",
        "fieldtype": "Select",
        "label": "Risk Type",
        "options": "Delay\nMaterial\nQuality\nResource",
        "insert_after": "risk_score"
    },
    {
        "fieldname": "risk_mitigation",
        "fieldtype": "Small Text",
        "label": "Risk Mitigation",
        "insert_after": "risk_type"
    },
    
    # Resource Leveling Fields
    {
        "fieldname": "was_shifted",
        "fieldtype": "Check",
        "label": "Was Shifted",
        "insert_after": "risk_mitigation"
    },
    {
        "fieldname": "original_workstation",
        "fieldtype": "Link",
        "label": "Original Workstation",
        "options": "APS Workstation",
        "depends_on": "eval:doc.was_shifted==1",
        "insert_after": "was_shifted"
    },
    {
        "fieldname": "shift_reason",
        "fieldtype": "Small Text",
        "label": "Shift Reason",
        "depends_on": "eval:doc.was_shifted==1",
        "insert_after": "original_workstation"
    },
    
    # ML Predictions Fields
    {
        "fieldname": "predicted_duration_hours",
        "fieldtype": "Float",
        "label": "Predicted Duration (Hours)",
        "insert_after": "shift_reason"
    },
    {
        "fieldname": "prediction_confidence",
        "fieldtype": "Percent",
        "label": "Prediction Confidence",
        "insert_after": "predicted_duration_hours"
    },
    {
        "fieldname": "actual_duration_hours",
        "fieldtype": "Float",
        "label": "Actual Duration (Hours)",
        "description": "Filled after execution for ML training",
        "insert_after": "prediction_confidence"
    }
]

## ===========================================
## APS PRODUCTION PLANNING WORKSTATION SCHEDULE
## Add these fields
## ===========================================

APS_PRODUCTION_PLANNING_WORKSTATION_SCHEDULE_FIELDS = [
    # Resource Info
    {
        "fieldname": "load_percentage",
        "fieldtype": "Percent",
        "label": "Load %",
        "in_list_view": 1,
        "insert_after": "duration_mins"  # Adjust based on existing
    },
    {
        "fieldname": "is_overtime",
        "fieldtype": "Check",
        "label": "Overtime",
        "insert_after": "load_percentage"
    },
    {
        "fieldname": "overtime_hours",
        "fieldtype": "Float",
        "label": "Overtime Hours",
        "depends_on": "eval:doc.is_overtime==1",
        "insert_after": "is_overtime"
    },
    
    # Batching
    {
        "fieldname": "batch_id",
        "fieldtype": "Data",
        "label": "Batch ID",
        "insert_after": "overtime_hours"
    },
    {
        "fieldname": "is_first_in_batch",
        "fieldtype": "Check",
        "label": "First in Batch",
        "insert_after": "batch_id"
    },
    {
        "fieldname": "is_last_in_batch",
        "fieldtype": "Check",
        "label": "Last in Batch",
        "insert_after": "is_first_in_batch"
    },
    
    # Leveling
    {
        "fieldname": "was_shifted_here",
        "fieldtype": "Check",
        "label": "Shifted Here",
        "insert_after": "is_last_in_batch"
    },
    {
        "fieldname": "original_workstation",
        "fieldtype": "Link",
        "label": "Original Workstation",
        "options": "APS Workstation",
        "depends_on": "eval:doc.was_shifted_here==1",
        "insert_after": "was_shifted_here"
    },
    
    # Actual vs Planned
    {
        "fieldname": "actual_start_datetime",
        "fieldtype": "Datetime",
        "label": "Actual Start",
        "insert_after": "original_workstation"
    },
    {
        "fieldname": "actual_end_datetime",
        "fieldtype": "Datetime",
        "label": "Actual End",
        "insert_after": "actual_start_datetime"
    },
    {
        "fieldname": "variance_mins",
        "fieldtype": "Float",
        "label": "Variance (Mins)",
        "description": "actual - planned",
        "read_only": 1,
        "insert_after": "actual_end_datetime"
    },
    {
        "fieldname": "delay_reason",
        "fieldtype": "Small Text",
        "label": "Delay Reason",
        "insert_after": "variance_mins"
    }
]

## ===========================================
## APS PLANNING BOTTLENECK
## Add these fields
## ===========================================

APS_PLANNING_BOTTLENECK_FIELDS = [
    # ML Prediction
    {
        "fieldname": "ml_model_version",
        "fieldtype": "Data",
        "label": "ML Model Version",
        "insert_after": "bottleneck_severity"  # Adjust based on existing
    },
    {
        "fieldname": "confidence_level",
        "fieldtype": "Percent",
        "label": "Confidence Level",
        "insert_after": "ml_model_version"
    },
    {
        "fieldname": "prediction_features",
        "fieldtype": "Long Text",
        "label": "Prediction Features (JSON)",
        "insert_after": "confidence_level"
    },
    
    # Validation
    {
        "fieldname": "actual_occurred",
        "fieldtype": "Check",
        "label": "Actually Occurred",
        "insert_after": "prediction_features"
    },
    {
        "fieldname": "actual_delay_hours",
        "fieldtype": "Float",
        "label": "Actual Delay (Hours)",
        "depends_on": "eval:doc.actual_occurred==1",
        "insert_after": "actual_occurred"
    },
    {
        "fieldname": "prediction_accuracy_score",
        "fieldtype": "Percent",
        "label": "Prediction Accuracy",
        "description": "For model improvement",
        "read_only": 1,
        "insert_after": "actual_delay_hours"
    }
]

## ===========================================
## APS JOB CARD
## Add these fields (if not already present)
## ===========================================

APS_JOB_CARD_FIELDS = [
    # Scheduling Info
    {
        "fieldname": "scheduling_section",
        "fieldtype": "Section Break",
        "label": "Scheduling Info",
        "collapsible": 1,
        "insert_after": "status"  # Adjust based on existing
    },
    {
        "fieldname": "is_schedulable",
        "fieldtype": "Check",
        "label": "Is Schedulable",
        "default": "1",
        "insert_after": "scheduling_section"
    },
    {
        "fieldname": "priority_score",
        "fieldtype": "Float",
        "label": "Priority Score (0-100)",
        "insert_after": "is_schedulable"
    },
    {
        "fieldname": "complexity_score",
        "fieldtype": "Float",
        "label": "Complexity Score (0-10)",
        "insert_after": "priority_score"
    },
    {
        "fieldname": "column_break_sched_1",
        "fieldtype": "Column Break",
        "insert_after": "complexity_score"
    },
    {
        "fieldname": "skill_required",
        "fieldtype": "Select",
        "label": "Skill Required",
        "options": "Low\nMedium\nHigh\nExpert",
        "insert_after": "column_break_sched_1"
    },
    {
        "fieldname": "is_splittable",
        "fieldtype": "Check",
        "label": "Can Split",
        "insert_after": "skill_required"
    },
    {
        "fieldname": "is_shiftable",
        "fieldtype": "Check",
        "label": "Can Shift Resource",
        "insert_after": "is_splittable"
    },
    
    # Historical Data
    {
        "fieldname": "historical_section",
        "fieldtype": "Section Break",
        "label": "Historical Data",
        "collapsible": 1,
        "insert_after": "is_shiftable"
    },
    {
        "fieldname": "historical_duration_avg",
        "fieldtype": "Float",
        "label": "Historical Avg Duration (Hours)",
        "read_only": 1,
        "insert_after": "historical_section"
    },
    {
        "fieldname": "historical_duration_std",
        "fieldtype": "Float",
        "label": "Historical Duration Std Dev",
        "read_only": 1,
        "insert_after": "historical_duration_avg"
    },
    {
        "fieldname": "delay_history",
        "fieldtype": "Long Text",
        "label": "Delay History (JSON)",
        "description": "For ML training",
        "insert_after": "historical_duration_std"
    }
]

## ===========================================
## APS WORKSTATION
## Add these fields (if not already present)
## ===========================================

APS_WORKSTATION_FIELDS = [
    # ML Features
    {
        "fieldname": "ml_features_section",
        "fieldtype": "Section Break",
        "label": "ML Features",
        "collapsible": 1,
        "insert_after": "capacity"  # Adjust based on existing
    },
    {
        "fieldname": "skill_level",
        "fieldtype": "Select",
        "label": "Skill Level",
        "options": "1\n2\n3\n4\n5",
        "default": "3",
        "insert_after": "ml_features_section"
    },
    {
        "fieldname": "reliability_score",
        "fieldtype": "Percent",
        "label": "Reliability Score",
        "description": "Based on breakdown history",
        "insert_after": "skill_level"
    },
    {
        "fieldname": "maintenance_due_date",
        "fieldtype": "Date",
        "label": "Maintenance Due Date",
        "insert_after": "reliability_score"
    },
    {
        "fieldname": "column_break_ml_1",
        "fieldtype": "Column Break",
        "insert_after": "maintenance_due_date"
    },
    {
        "fieldname": "breakdown_probability",
        "fieldtype": "Percent",
        "label": "Breakdown Probability",
        "description": "ML predicted",
        "read_only": 1,
        "insert_after": "column_break_ml_1"
    },
    {
        "fieldname": "historical_utilization_avg",
        "fieldtype": "Percent",
        "label": "Historical Avg Utilization",
        "read_only": 1,
        "insert_after": "breakdown_probability"
    },
    
    # Scheduling
    {
        "fieldname": "scheduling_options_section",
        "fieldtype": "Section Break",
        "label": "Scheduling Options",
        "collapsible": 1,
        "insert_after": "historical_utilization_avg"
    },
    {
        "fieldname": "allow_overtime",
        "fieldtype": "Check",
        "label": "Allow Overtime",
        "insert_after": "scheduling_options_section"
    },
    {
        "fieldname": "overtime_cost_multiplier",
        "fieldtype": "Float",
        "label": "Overtime Cost Multiplier",
        "default": "1.5",
        "depends_on": "eval:doc.allow_overtime==1",
        "insert_after": "allow_overtime"
    },
    {
        "fieldname": "column_break_sched_1",
        "fieldtype": "Column Break",
        "insert_after": "overtime_cost_multiplier"
    },
    {
        "fieldname": "max_overtime_hours_per_day",
        "fieldtype": "Float",
        "label": "Max Overtime Hours/Day",
        "depends_on": "eval:doc.allow_overtime==1",
        "insert_after": "column_break_sched_1"
    },
    {
        "fieldname": "eligible_for_shift",
        "fieldtype": "Check",
        "label": "Eligible for Job Shifting",
        "default": "1",
        "insert_after": "max_overtime_hours_per_day"
    }
]

# Total fields to add:
TOTAL_FIELDS = {
    "APS Production Planning Result": len(APS_PRODUCTION_PLANNING_RESULT_FIELDS),
    "APS Production Planning Item Result": len(APS_PRODUCTION_PLANNING_ITEM_RESULT_FIELDS),
    "APS Production Planning Workstation Schedule": len(APS_PRODUCTION_PLANNING_WORKSTATION_SCHEDULE_FIELDS),
    "APS Planning Bottleneck": len(APS_PLANNING_BOTTLENECK_FIELDS),
    "APS Job Card": len(APS_JOB_CARD_FIELDS),
    "APS Workstation": len(APS_WORKSTATION_FIELDS)
}

print("="*60)
print("FIELDS TO ADD - SCHEDULE OPTIMIZATION")
print("="*60)
for doctype, count in TOTAL_FIELDS.items():
    print(f"{doctype}: {count} fields")
print("="*60)
print(f"TOTAL FIELDS TO ADD: {sum(TOTAL_FIELDS.values())}")
print("="*60)
