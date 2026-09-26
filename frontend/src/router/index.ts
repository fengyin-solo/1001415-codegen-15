import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Vehicle = () => import('@/views/vehicle/index.vue')
const Driver = () => import('@/views/driver/index.vue')
const Route = () => import('@/views/route/index.vue')
const Task = () => import('@/views/task/index.vue')
const Tempmonitor = () => import('@/views/tempmonitor/index.vue')
const Coldroom = () => import('@/views/coldroom/index.vue')
const Goods = () => import('@/views/goods/index.vue')
const Loading = () => import('@/views/loading/index.vue')
const Delivery = () => import('@/views/delivery/index.vue')
const Anomaly = () => import('@/views/anomaly/index.vue')
const Maintenance = () => import('@/views/maintenance/index.vue')
const Refuel = () => import('@/views/refuel/index.vue')
const Clean = () => import('@/views/clean/index.vue')
const Shift = () => import('@/views/shift/index.vue')
const TransportContract = () => import('@/views/transport_contract/index.vue')
const Insurance = () => import('@/views/insurance/index.vue')
const Customer = () => import('@/views/customer/index.vue')
const DailyStats = () => import('@/views/daily_stats/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/vehicle', name: 'vehicle', component: Vehicle },
    { path: '/driver', name: 'driver', component: Driver },
    { path: '/route', name: 'route', component: Route },
    { path: '/task', name: 'task', component: Task },
    { path: '/tempmonitor', name: 'tempmonitor', component: Tempmonitor },
    { path: '/coldroom', name: 'coldroom', component: Coldroom },
    { path: '/goods', name: 'goods', component: Goods },
    { path: '/loading', name: 'loading', component: Loading },
    { path: '/delivery', name: 'delivery', component: Delivery },
    { path: '/anomaly', name: 'anomaly', component: Anomaly },
    { path: '/maintenance', name: 'maintenance', component: Maintenance },
    { path: '/refuel', name: 'refuel', component: Refuel },
    { path: '/clean', name: 'clean', component: Clean },
    { path: '/shift', name: 'shift', component: Shift },
    { path: '/transport_contract', name: 'transport_contract', component: TransportContract },
    { path: '/insurance', name: 'insurance', component: Insurance },
    { path: '/customer', name: 'customer', component: Customer },
    { path: '/daily_stats', name: 'daily_stats', component: DailyStats },
  ],
})

export default router
