<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">冷链物流配送管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向冷藏车调度、温控记录、生鲜配送、冷库管理、运输签收与温控异常处置的一体化冷链物流管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "冷藏车辆", path: "/vehicle" }, { label: "驾驶员管理", path: "/driver" }, { label: "配送线路", path: "/route" }, { label: "配送任务单", path: "/task" }, { label: "温控记录", path: "/tempmonitor" }, { label: "冷库管理", path: "/coldroom" }, { label: "货品信息", path: "/goods" }, { label: "装车核对", path: "/loading" }, { label: "到站签收", path: "/delivery" }, { label: "温控异常", path: "/anomaly" }, { label: "车辆维保", path: "/maintenance" }, { label: "油料管理", path: "/refuel" }, { label: "箱体清洁", path: "/clean" }, { label: "排班管理", path: "/shift" }, { label: "运输合同", path: "/transport_contract" }, { label: "保险管理", path: "/insurance" }, { label: "收货方管理", path: "/customer" }, { label: "运营日报", path: "/daily_stats" }]
</script>
