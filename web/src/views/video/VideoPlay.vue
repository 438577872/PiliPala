<template>
  <div>
    <AccountHeader></AccountHeader>
    <el-row>
      <el-col :offset="4" :span="20">

        <h3 style="line-height: 50px">
          <el-tag type="danger" size="middle" style="background: pink;color: white">
            活动作品
          </el-tag>
          {{video.title}}
        </h3>
        <div style="font-size: 12px;color: rgb(153,153,153);line-height: 32px">
          19.1万播放 · 743弹幕 2021-04-18 13:38:22
        </div>
        <el-row>
          <el-col :span="14">
            <Player :src="video.src" :form="form" :barrage="barrage"></Player>
          </el-col>
          <el-col :offset="1" :span="6">
            <VideoRightComponent :nos="nos"  :barrage="barrage" @changeVideo="changeVideo"/>
          </el-col>
        </el-row>
        <el-row style="margin: 20px;font-size: 10px">
          <el-col>
            未经作者授权，禁止转载
          </el-col>
          <el-col>
            大家好，我是王冰冰，真以为我不上B站么
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <VideoComment ></VideoComment>
          </el-col>
        </el-row>
      </el-col>
    </el-row>

  </div>
</template>

<script>
    import AccountHeader from "@/views/account/AccountHeader";
    import {fetchBarrageBySeriesId, fetchVideoNos, getVideoUrlBySeriesIdAndNo} from "@/api/VideoApi";
    import Player from "@/views/video/VideoPlayer";
    import VideoComment from "@/views/video/VideoComment";
    import VideoRightComponent from "@/views/video/VideoRightComponent";

    export default {
        name: "VideoPlay",
        components: {
            VideoRightComponent,
            VideoComment,
            Player,
            AccountHeader
        },
        data() {
            return {
                form: {
                    series_id: '',
                    no: ''
                },
                video: {
                    src: '',
                    title: ''
                },
                isOk: false,
                barrage: [],

                nos: []
            }
        },
        methods: {
            init() {
                let args = this.$route.query
                let series_id = args.series_id
                this.form.no = args.no
                this.form.series_id = series_id
                this.series_id = series_id
                getVideoUrlBySeriesIdAndNo(args).then(resp => {
                    this.video.src = '/static/video/' + resp.data.resource_url
                    this.video.title = resp.data.title
                }).then(() => {
                    fetchVideoNos(args).then(resp => {
                        this.nos = resp.data
                    })
                }).then(() => {
                    this.fetchBarrageBySeriesId()
                })
            },
            fetchBarrageBySeriesId() {
                fetchBarrageBySeriesId(this.form)
                    .then(resp => {
                        this.barrage = resp.data
                    })
            },
            changeVideo(no) {
                this.form.no = no
                getVideoUrlBySeriesIdAndNo(this.form)
                    .then(resp => {
                        this.video.src = '/static/video/' + resp.data.resource_url
                        this.video.title = resp.data.title
                    })
                    .then(() => {
                        this.fetchBarrageBySeriesId()
                    })
            }
        },
        mounted() {
            this.init()

        }
    }
</script>

<style scoped>

</style>
