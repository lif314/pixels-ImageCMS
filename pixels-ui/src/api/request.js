// 随axios进行二次封装
import axios from 'axios'
// 引入进度条
import nprogress from 'nprogress'
import "nprogress/nprogress.css"

// 1、利用axios创建一个axios实例
const requests = axios.create({
    baseURL: "/api",
    timeout: 5000 //请求超时时间 5s
})


// 2、请求拦截器
requests.interceptors.request.use((config) => {
    // 启动进度条
    nprogress.start()
    // 可以在config中添加参数
    // TODO token认证
    return config;
})

// 3、响应拦截器
requests.interceptors.response.use((res) => {
    // nprogress进度条结束
    nprogress.done()
    return res.data; // 返回数据
}, (err) => {
    return Promise.reject(new Error(err.message))
})

export default requests