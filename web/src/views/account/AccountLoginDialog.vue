<template>
  <div style=";z-index: -1;text-align: center">
    <div>
      <router-link to="/login"  >
        <el-button type="primary" style="width: 100%;color: white">立即登录</el-button>
      </router-link>
    </div>
    <div style="margin-top: 10px">
      首次登录?
      <el-link>
        点击注册
      </el-link>
    </div>
  </div>
</template>

<script>
    export default {
        name: "AccountLoginDialog"
    }
</script>

<style scoped>

</style>
