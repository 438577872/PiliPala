<template>
  <el-card style="min-height: 500px">
    <SpaceTitleFont title="我的频道"></SpaceTitleFont>
    <div align="center" style="margin-top: 60px">
      <p class="font-dark-gray">你可以将自己上传的视频整理成 <span class="primary">“频道”</span></p>
      <p class="font-dark-gray">方便别人查看，快去创建频道吧~</p>

      <!--      <p style="background-image: url(//s1.hdslb.com/bfs/static/jinkela/space/assets/empty-channel.png);width: 600px;height: 400px">-->

      <!--      </p>-->
      <el-image src="//s1.hdslb.com/bfs/static/jinkela/space/assets/empty-channel.png" style=";margin-top: 20px"></el-image>
      <p>
        <el-button type="primary" style="color: white;margin-top: 20px" >+ 创建频道</el-button>
      </p>
    </div>
  </el-card>
</template>

<script>
    import SpaceTitleFont from "@/views/space/components/SpaceTitleFont";

    export default {
        name: "SpaceChannel",
        components: {SpaceTitleFont}
    }
</script>

<style scoped>

</style>
