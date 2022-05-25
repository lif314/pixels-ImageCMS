<template>
  <div id="app" class="app">
      <router-view></router-view>
     <el-backtop target=".app"> <i class="el-icon-caret-top"></i></el-backtop>
  </div>
</template>

<script>

export default {
  name: "App",
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body{
  background-color:skyblue;
}

/* #nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
} */

/*配置快速回到顶栏 */
.app{
  height:98vh;
  overflow-x: hidden;
}
</style>
