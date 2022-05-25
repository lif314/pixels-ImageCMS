// 全局小仓库
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

// 引入小仓库
import user from './user'
import image from './image'

export default new Vuex.Store({
    modules:{
        user,
        image
    }
})


