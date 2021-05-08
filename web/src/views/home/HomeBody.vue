<template>
  <div>
    <el-row style="height:100px;;">
      <el-col :span="20" :offset="2">
        <HomeNav :iconSize="iconSize" :actives="actives" :types="types"></HomeNav>
        <HomeRecommend :carousels="carousels" :videos="videos"></HomeRecommend>
        <HomeOtherContents v-for="promotion in modules" :key="promotion.name" :promotions="promotion.list"
                           :title="promotion.name">
          <template slot="icon">
            <IconVoice></IconVoice>
          </template>
        </HomeOtherContents>

      </el-col>
    </el-row>
  </div>
</template>

<script>
    import IconHome from "@/components/icons/IconHome";
    import IconVoice from "@/components/icons/IconVoice";
    import HomeNav from "@/views/home/HomeNav";
    import HomeRecommend from "@/views/home/HomeRecommend";
    import HomeOtherContents from "@/views/home/HomeOtherContents";
    import {homeInit} from "@/api/HomeApi";

    export default {
        name: "HomeBody",
        components: {
            HomeOtherContents,
            HomeRecommend,
            HomeNav,
            IconVoice,
            IconHome
        },
        data() {
            return {
                value2: 20,
                types: null,
                actives: null,
                carousels: null,
                videos: null,
                promotions: null,
                iconSize: 20,
                shadowIndex: -1,
                modules: null
            }
        },
        methods: {
            to(url) {
                this.$router.push(url)
            }
        },
        mounted() {


            homeInit().then(resp => {
                let {types, actives, carousels, videos, promotions, modules} = resp.data
                this.types = types
                this.actives = actives
                this.carousels = carousels
                this.videos = videos
                this.promotions = promotions
                this.modules = modules

            })
        }
    }
</script>

<style scoped>

</style>
<style>

</style>
