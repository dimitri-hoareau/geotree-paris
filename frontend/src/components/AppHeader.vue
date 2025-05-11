<template>
    <header class="app-header">
      <div class="header-content">
        <div class="logo-title">
          <span class="logo">🌳</span>
          <h1 class="title">CaterpillarAlert Paris</h1>
        </div>
      </div>
    </header>
  </template>
  
  
  <style scoped>
    .app-header {
      background-color: #ffffff;
      border-bottom: 1px solid #e0e0e0;
      padding: var(--space-3) var(--space-4);
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    .logo-title {
      display: flex;
      align-items: center;
      gap: var(--space-2);
    }

    .logo {
      font-size: var(--font-size-xl);
    }

    .title {
      font-size: var(--font-size-lg);
      font-weight: 600;
      color: #2e7d32;
      margin: 0;
    }
  
  </style>