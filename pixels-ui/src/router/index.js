// 配置路由信息
import Vue from 'vue'
import VueRouter from 'vue-router'

// 重写push和replace函数

let originPush = VueRouter.prototype.push;
let originReplace = VueRouter.prototype.replace;
/**
 * @param {*} location 向哪里跳转 
 */
VueRouter.prototype.push = function (location, resolve, reject) {
    if (resolve && reject) {
        // call与apply的区别
        originPush.call(this, location, resolve, reject)
    } else {
        // 传入回调函数
        originPush.call(this, location, () => { }, () => { })
    }
}
VueRouter.prototype.replace = function (location, resolve, reject) {
    if (resolve && reject) {
        // call与apply的区别
        originReplace.call(this, location, resolve, reject)
    } else {
        // 传入成功和失败的回调函数
        originReplace.call(this, location, () => { }, () => { })
    }
}

// 使用路由
Vue.use(VueRouter)

const router = new VueRouter({
    routes:[
        {
            // 重定向
            path: '/',
            redirect: '/home'
        },
        {
            path: '/home',
            component: ()=>import("@/views/Home")
        },
        {
            path: '/register',
            component: ()=>import("@/views/Register")
        },
        {
            path: '/login',
            component: ()=>import("@/views/Login")
        },
        {
            path: '/upload',
            component: ()=>import("@/views/UploadFile")
        }
    ]
})

export default router



