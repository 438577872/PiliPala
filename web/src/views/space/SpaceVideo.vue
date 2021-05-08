<template>

  <el-row>
    <el-col style="padding: 20px">
      <el-row>
        <SpaceTitleFont title="我的视频"></SpaceTitleFont>
      </el-row>
      <el-row :gutter="10" v-loading="loading">
        <div align="center" v-if="!haveData">
          <el-image src="https://s1.hdslb.com/bfs/static/jinkela/space/assets/nodata02.png"></el-image>
          <p class="font-dark-gray" style="line-height:0px">空间主人还没有投过视频哦~</p>
        </div>
        <SpaceVideoList @finishLoading="finishLoading"></SpaceVideoList>

      </el-row>
    </el-col>
  </el-row>

</template>

<script>
    import SpaceTitleFont from "@/views/space/components/SpaceTitleFont";
    import SpaceVideoList from "@/views/space/components/SpaceVideoList";
    import {mapGetters} from "vuex";
    // import ma
    export default {
        name: "SpaceVideo",
        components: {SpaceVideoList, SpaceTitleFont},
        // compute
        computed: {
            ...mapGetters([
                'avatar'
            ])
        },
        data: () => ({
            loading: true,
            haveData: false

        }),
        methods: {
            finishLoading() {
                this.loading = false
                this.haveData = true
            }
        }
    }
</script>

<style scoped lang="scss">
  .active {
    background: #000;
  }
</style>
