import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

// 全局引入ElementUI
Vue.use(ElementUI);
Vue.config.productionTip = false
// 引入路由
import router from '@/router'
// 使用vuex
import store from '@/vuex/store'


new Vue({
  render: h => h(App),
  router: router, // 注册路由
  store,   //注册仓库  $store
}).$mount('#app')
