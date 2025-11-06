# Schedule Optimization DocTypes - Installation Guide

## 📦 Package Contents

This package contains DocType JSON files for the APS Schedule Optimization module.

### New DocTypes (9 files)
1. `1_aps_schedule_optimization_config.json` - Settings (Single DocType)
2. `2_aps_batch_schedule.json` - Batch schedules
3. `3_aps_batch_schedule_item.json` - Child table for batch items
4. `4_aps_batch_setup_requirement.json` - Child table for setup requirements
5. `5_aps_scenario_comparison.json` - Scenario comparison
6. `6_aps_scenario_comparison_detail.json` - Child table for scenarios
7. `7_aps_ml_model.json` - ML model management
8. `8_aps_optimization_run_log.json` - Run logs
9. `9_aps_risk_alert.json` - Risk alerts

### Fields to Add (1 file)
10. `fields_to_add.py` - Python script with all fields to add to existing DocTypes

---

## 🚀 Installation Steps

### Phase 1: Import New DocTypes (Required)

**Option A: Using Bench (Recommended)**

```bash
# Copy JSON files to your app
cp *.json /path/to/frappe-bench/apps/dbiz_aps/dbiz_aps/dbiz_aps/doctype/

# Import via bench
cd /path/to/frappe-bench
bench --site your-site migrate
```

**Option B: Using UI (Manual)**

For each JSON file:
1. Login to Frappe/ERPNext
2. Go to: **Developer > DocType > New DocType**
3. Click **Menu (⋮) > Import**
4. Upload the JSON file
5. Click **Save**

**Import Order (Important):**
```
1. aps_schedule_optimization_config.json (Settings)
2. aps_batch_schedule_item.json (Child table)
3. aps_batch_setup_requirement.json (Child table)
4. aps_batch_schedule.json (Parent)
5. aps_scenario_comparison_detail.json (Child table)
6. aps_scenario_comparison.json (Parent)
7. aps_ml_model.json
8. aps_optimization_run_log.json
9. aps_risk_alert.json
```

---

### Phase 2: Add Fields to Existing DocTypes (Required)

Open `fields_to_add.py` to see all fields that need to be added.

**For each DocType listed:**

1. Go to: **Customization > Customize Form**
2. Select the DocType (e.g., "APS Production Planning Result")
3. Add each field from the list:
   - Click **Add Row** in Fields table
   - Fill in: fieldname, fieldtype, label, options (if applicable)
   - Set insert_after to place field correctly
   - Set depends_on if field has conditional display
4. Click **Save**

**DocTypes to Customize:**
- ✅ APS Production Planning Result (63 fields)
- ✅ APS Production Planning Item Result (21 fields)
- ✅ APS Production Planning Workstation Schedule (13 fields)
- ✅ APS Planning Bottleneck (6 fields)
- ✅ APS Job Card (13 fields)
- ✅ APS Workstation (13 fields)

**Total: 129 fields to add**

---

### Phase 3: Set Permissions

For each new DocType, set permissions:

1. Go to: **Users & Permissions > Role Permission Manager**
2. Select DocType
3. Set permissions:

```
System Manager: Full access (Create, Read, Write, Delete)
Manufacturing Manager: Create, Read, Write
Manufacturing User: Read only
```

---

## 🔧 Post-Installation Configuration

### 1. Configure Settings

Go to: **APS Schedule Optimization Config**

Set default values:
- Default AI Algorithm: Hybrid
- Default Optimization Objective: Minimize Makespan
- Max Utilization: 85%
- Enable Batching: Yes
- Enable ML Predictions: Yes
- ML Confidence Threshold: 70%

### 2. Verify Installation

Run this in Python console to verify:

```python
import frappe

# Check new DocTypes
doctypes = [
    "APS Schedule Optimization Config",
    "APS Batch Schedule",
    "APS Scenario Comparison",
    "APS ML Model",
    "APS Optimization Run Log",
    "APS Risk Alert"
]

for dt in doctypes:
    if frappe.db.exists("DocType", dt):
        print(f"✅ {dt}")
    else:
        print(f"❌ {dt} - MISSING!")

# Check added fields
fields_to_check = {
    "APS Production Planning Result": ["ai_algorithm_used", "batching_enabled", "ml_enabled"],
    "APS Production Planning Item Result": ["batch_id", "is_critical_path", "risk_score"],
    "APS Production Planning Workstation Schedule": ["load_percentage", "batch_id"]
}

print("\n--- Checking Added Fields ---")
for doctype, fields in fields_to_check.items():
    meta = frappe.get_meta(doctype)
    for field in fields:
        if meta.has_field(field):
            print(f"✅ {doctype}.{field}")
        else:
            print(f"❌ {doctype}.{field} - MISSING!")
```

---

## 📊 Field Summary

### APS Production Planning Result
**63 new fields** organized in sections:
- Schedule Optimization Settings (3 fields)
- Critical Path Analysis (5 fields)
- Batching (7 fields)
- Resource Leveling (7 fields)
- Constraint Programming (7 fields)
- ML Predictions (7 fields)
- Parallel Processing (5 fields)
- Links (2 fields)

### APS Production Planning Item Result
**21 new fields:**
- Batching (4 fields)
- Critical Path (6 fields)
- Risk Assessment (3 fields)
- Resource Leveling (3 fields)
- ML Predictions (3 fields)
- Actual tracking (2 fields)

### APS Production Planning Workstation Schedule
**13 new fields:**
- Resource Info (3 fields)
- Batching (3 fields)
- Leveling (2 fields)
- Actual vs Planned (5 fields)

### APS Planning Bottleneck
**6 new fields:**
- ML Prediction (3 fields)
- Validation (3 fields)

### APS Job Card
**13 new fields:**
- Scheduling Info (7 fields)
- Historical Data (3 fields)

### APS Workstation
**13 new fields:**
- ML Features (6 fields)
- Scheduling Options (5 fields)

---

## 🧪 Testing

After installation, test with a simple scenario:

```python
import frappe

# Create a test schedule optimization config
config = frappe.get_single("APS Schedule Optimization Config")
config.default_ai_algorithm = "Hybrid"
config.save()

# Create a test batch schedule
batch = frappe.new_doc("APS Batch Schedule")
batch.batch_name = "Test Batch 001"
batch.batch_type = "Product Family"
batch.status = "Planned"
batch.insert()

print(f"Test batch created: {batch.name}")

# Create a test scenario comparison
scenario = frappe.new_doc("APS Scenario Comparison")
scenario.comparison_date = frappe.utils.today()
scenario.primary_objective = "Makespan"
scenario.insert()

print(f"Test scenario created: {scenario.name}")
```

---

## 📝 Migration Script (Optional)

If you have existing data, create a migration script:

```python
# dbiz_aps/patches/v1_0/add_schedule_optimization_fields.py

import frappe

def execute():
    """
    Migration script to populate default values for new fields
    """
    
    # Update existing Production Planning Results
    results = frappe.get_all("APS Production Planning Result",
        filters={"planning_type": "Production Planning"},
        pluck="name"
    )
    
    for result_id in results:
        doc = frappe.get_doc("APS Production Planning Result", result_id)
        
        # Set default values for new fields
        doc.db_set("batching_enabled", 0, update_modified=False)
        doc.db_set("leveling_applied", 0, update_modified=False)
        doc.db_set("ml_enabled", 0, update_modified=False)
        doc.db_set("parallel_mode", "Single", update_modified=False)
    
    frappe.db.commit()
    print(f"Updated {len(results)} records")
```

---

## ⚠️ Known Issues

1. **Field Order**: After adding fields via Customize Form, you may need to reorder them manually
2. **Depends On**: Some conditional fields may not work until the parent field has a value
3. **Performance**: With 129 new fields, consider indexing important fields like:
   - `batch_id`
   - `is_critical_path`
   - `risk_score`
   - `ml_confidence_level`

---

## 🆘 Troubleshooting

### Issue: "DocType not found"
**Solution:** Import child tables before parent tables

### Issue: "Field already exists"
**Solution:** Skip that field or delete existing field first

### Issue: "Cannot import JSON"
**Solution:** Check JSON syntax, ensure all required fields present

### Issue: "Permission denied"
**Solution:** Check if you're logged in as System Manager

---

## 📞 Support

For issues or questions:
1. Check the `fields_to_add.py` file for complete field definitions
2. Review Frappe documentation: https://frappeframework.com/docs
3. Check field dependencies and insert_after values

---

## ✅ Checklist

- [ ] Imported all 9 new DocTypes
- [ ] Added fields to APS Production Planning Result (63 fields)
- [ ] Added fields to APS Production Planning Item Result (21 fields)
- [ ] Added fields to APS Production Planning Workstation Schedule (13 fields)
- [ ] Added fields to APS Planning Bottleneck (6 fields)
- [ ] Added fields to APS Job Card (13 fields)
- [ ] Added fields to APS Workstation (13 fields)
- [ ] Set permissions for all new DocTypes
- [ ] Configured APS Schedule Optimization Config
- [ ] Tested with sample data
- [ ] Ran migration script (if needed)

---

## 📚 Next Steps

After installation:
1. Implement the optimization algorithms (see algorithm documentation)
2. Create the main function `run_schedule_optimization()`
3. Add API endpoint for frontend
4. Create UI forms for input parameters
5. Build Gantt chart visualization
6. Train ML models with historical data

---

**Installation Date:** _____________

**Installed By:** _____________

**Notes:** _____________
