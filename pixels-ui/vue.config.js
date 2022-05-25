const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    proxy: {
      '/api': {    //将www.exaple.com印射为/api
        target: 'http://localhost:5000',  // 接口域名
        secure: false,  // 如果是https接口，需要配置这个参数
        pathRewrite: {
          '^/api': ''   //需要rewrite的,
        }
      }
    }
  }
})
