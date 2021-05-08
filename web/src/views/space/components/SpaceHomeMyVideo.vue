<template>
  <div>
    <el-col :span="4">
      <h3>我的视频</h3>
    </el-col>
    <el-col>
      <div>
        <SpaceVideoList @finishLoading="finishLoading"></SpaceVideoList>
      </div>
    </el-col>
    <el-col v-if="!haveData" :offset="9" :span="8" style="font-size: 13px;padding-top: 10px">
      <div>
        <span
            class="font-dark-gray">还没有上传过视频哦~
      </span>
        <router-link to="/space/upload">
          <span class="primary" style="margin-left: 20px">
            立即上传
          </span>
        </router-link>
      </div>
    </el-col>
  </div>
</template>

<script>
    import SpaceVideoList from "@/views/space/components/SpaceVideoList";

    export default {
        name: "SpaceHomeMyVideo",
        components: {SpaceVideoList},
        data: () => ({
            video_list: null,
            haveData: false
        }),
        methods: {
            finishLoading() {
                this.haveData = true
            }
        }
    }
</script>

<style scoped>

</style>
