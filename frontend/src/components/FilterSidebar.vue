<template>
  <aside class="filter-sidebar">
    <div class="sidebar-section">
      <h3 class="section-title">Filters</h3>
      <div class="filter-option">
        <label class="filter-label">
          <div class="custom-checkbox">
            <input type="checkbox" class="filter-checkbox" />
            <span class="checkmark"></span>
          </div>
          <span class="filter-text">Risky Trees 🌲</span>
        </label>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.filter-sidebar {
  width: 450px;
  padding: var(--space-4);
  height: 100%;
}

.sidebar-section {
  margin-bottom: var(--space-5);
}

.section-title {
  font-size: var(--font-size-md);
  font-weight: 600;
  margin-bottom: var(--space-3);
}

.filter-option {
  margin-bottom: var(--space-3);
  padding: var(--space-2) 0;
}

.filter-label {
  display: flex;
  cursor: pointer;
}

/* Hide original Checkbox*/
.filter-checkbox {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Create custom checkbox */
.custom-checkbox {
  position: relative;
  margin-right: var(--space-3);
}

.checkmark {
  position: relative;
  display: inline-block;
  height: 18px;
  width: 18px;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.filter-label:hover .checkmark {
  border-color: #2e7d32;
}

.filter-checkbox:checked + .checkmark {
  background-color: #2e7d32;
  border-color: #2e7d32;
}

.filter-checkbox:checked + .checkmark:after {
  content: "";
  position: absolute;
  left: 5px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.filter-text {
  font-size: var(--font-size-md);
  color: #666;
}
</style>
