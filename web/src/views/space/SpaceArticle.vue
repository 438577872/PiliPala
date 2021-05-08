<template>

  <el-row>
    <el-col style="padding: 20px">
      <el-row>
        <SpaceTitleFont title="专栏文章"/>
      </el-row>
      <el-row>
        <div align="center">
          <el-image src="https://s1.hdslb.com/bfs/static/jinkela/space/assets/nodata02.png"></el-image>
          <p class="font-dark-gray" style="line-height:0px">空间的主人还没有投过视频哦~~</p>
        </div>
      </el-row>
    </el-col>
  </el-row>

</template>

<script>
    import SpaceTitleFont from "@/views/space/components/SpaceTitleFont";

    export default {
        name: "SpaceArticle",
        components: {SpaceTitleFont},
        data() {
            return {}
        }
    }
</script>

<style scoped lang="scss">
  .active {
    background: #000;
  }
</style>
