<template>
  <el-card>
    <el-row>
      <el-col  style="padding: 20px">
        <el-row>
          <SpaceTitleFont title="我的音频"/>
        </el-row>
        <el-row>
          <div align="center">
            <el-image src="https://s1.hdslb.com/bfs/static/jinkela/space/assets/nodata02.png"></el-image>
            <p class="font-dark-gray" style="line-height:0px">空间的主人还没有关注过标签~~</p>
          </div>
        </el-row>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
    import SpaceTitleFont from "@/views/space/components/SpaceTitleFont";
    export default {
        name: "SpaceSubs",
        components: {SpaceTitleFont}
    }
</script>

<style scoped>

</style>
