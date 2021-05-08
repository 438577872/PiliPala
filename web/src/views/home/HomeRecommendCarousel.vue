<template>
  <el-col :span="8">
    <el-carousel height="270px">
      <el-carousel-item v-for="item in carousels" :key="item.url">
        <el-image
            :src="item.url" style="height: 100%;"></el-image>
      </el-carousel-item>
    </el-carousel>
  </el-col>
</template>

<script>
    export default {
        name: "HomeRecommendCarousel",
        props:['carousels']
    }
</script>

<style scoped>

</style>
