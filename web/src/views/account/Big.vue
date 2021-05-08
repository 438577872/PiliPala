<template>
  <div>
    <el-row>
      <el-col :span="8">
        <div style="float: left;">
          <el-avatar
              src="https://i2.hdslb.com/bfs/face/19b1200de0c721a090ab406910c8e5403dcdf163.jpg"></el-avatar>

        </div>
        <div style="float: left;margin-left: 20px">
          <b>吃花椒的喵酱</b>
          <br>
          <span style="color: gray;font-size: 10px">
                      升级大会员福利多多
                    </span>
        </div>
        <div style="clear: both;"></div>
      </el-col>
      <el-col :span="8" :offset="8">
        <el-button type="primary" style="color: white">开通大会员</el-button>
        <el-button>赠送</el-button>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <el-row>
      <el-carousel>
        <el-carousel-item v-for="item in 4" :key="item">
          <el-image
              src="https://i0.hdslb.com/bfs/archive/d78de336396be90946b039a9d7f32b38218c66b6.jpg"></el-image>
        </el-carousel-item>
      </el-carousel>
    </el-row>
    <el-divider></el-divider>
  </div>
</template>

<script>
    export default {
        name: "Big"
    }
</script>

<style scoped>

</style>
