<template>
  <el-row style="margin-top: 20px" :gutter="6">
    <HomeRecommendCarousel :carousels="carousels"/>
    <el-col :span="16">
      <el-col style="width: 13rem" v-for="(item,index) in videos" :key="item.url">
        <div style="position: relative;height: 130px;width: 100%;overflow: hidden;margin-bottom: 10px"
             class="shadow2"
             @mouseover="shadowIndex=index" @mouseout="shadowIndex=-1">
          <div style=";height: 130px">
            <el-image
                :src="item.url"></el-image>
          </div>
          <a :href="item.to" target="_blank">
            <div :id="index" class="s"
                 style="position: absolute;
                 z-index: 1;
                 height: 180px;
                 width: 100%;
                 top: 0;
                 padding-top: 50px;
                 padding-left: 5px;
                 padding-right: 5px;
                 color: white;
                 font-size: 14px;
                 line-height: 26px;
                 background:  linear-gradient(0deg, rgba(0,0,0,1), rgba(0,0,0,0));">
              <div style="margin-top: 50px">{{item.title}} <br>
                UP : {{item.up}} <br></div>
            </div>
          </a>
        </div>
      </el-col>
    </el-col>
  </el-row>
</template>

<script>
    import HomeRecommendCarousel from "@/views/home/HomeRecommendCarousel";

    export default {
        name: "HomeRecommend",
        components: {HomeRecommendCarousel},
        props: [
            'videos',
            'carousels'
        ]
    }
</script>

<style scoped>
  @keyframes example {
    from {
      /*top: 200px*/
    }
    to {
      top: -50px;
      padding-top: 30px;
    }
  }

  /* 向此元素应用动画效果 */
  .shadow {
    top: 60px;
    animation: alternate forwards;
    width: 100px;
    height: 100px;
    /*background-color: red;*/
    animation-name: example;
    animation-duration: 0.25s;
  }

  .s:hover {
    top: 60px;
    animation: alternate forwards;
    width: 100px;
    height: 100px;
    /*background-color: red;*/
    animation-name: example;
    animation-duration: 0.25s;
  }
</style>
