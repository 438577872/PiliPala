<template>
  <el-card body-style="padding:0">
    <div style="position: relative;overflow: hidden">
      <video-player class="video-player vjs-custom-skin"
                    ref="videoPlayer"
                    :playsinline="true"
                    :options="playerOptions"
                    @timeupdate="onPlayerTimeupdate($event)"
                    style="height: 540px;"
      />

      <div style="position: absolute;top: 0 ">
        <span class="barrage" v-for="(s,index) in list" v-if="s.show" style="z-index: 1;color: white;font-size: 20px"
              :style="{
          transform: `translateY(${s.translateY}px)  translateX(${s.translateX}px)`}">
          {{s.msg}}
        </span>
      </div>
      <el-input v-model="msg">
        <el-button slot="append" @click="send">
          发送
        </el-button>
      </el-input>
    </div>
  </el-card>
</template>
<script>
    import {sendBarrage} from "@/api/VideoApi";

    export default {
        name: 'Player',
        data() {
            return {
                // 视频播放
                playerOptions: {
                    playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
                    autoplay: false, //如果true,浏览器准备好时开始回放。
                    muted: false, // 默认情况下将会消除任何音频。
                    loop: false, // 导致视频一结束就重新开始。
                    preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                    language: 'zh-CN',
                    aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                    fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                    sources: [{
                        type: "",
                        // src: 'http://vjs.zencdn.net/v/oceans.mp4'//url地址
                        src: this.src
                        // src: "" //url地址
                    }],
                    poster: "", //你的封面地址
                    // width: document.documentElement.clientWidth,
                    notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                    controlBar: {
                        timeDivider: true,
                        durationDisplay: true,
                        remainingTimeDisplay: false,
                        fullscreenToggle: true  //全屏按钮
                    }
                },
                list: [],

                currentIndex2: 0,
                currentTime: 0,
                msg: '',


            }
        },
        props: ['src', 'barrage', "form"],
        watch: {
            src(newData, oldData) {
                this.playerOptions.sources[0].src = newData
            }
        },
        methods: {
            createY() {
                return Math.random() * 500
            },

            onPlayerTimeupdate(player) {
                this.currentTime = player.currentTime()
            },
            send() {
                sendBarrage({
                    msg: this.msg,
                    series_id: this.form.series_id,
                    time: this.currentTime,
                    no: this.form.no ? this.form.no : 1
                }).then(resp => {
                    if (resp.code === 20000) {
                        this.insert({
                            msg: this.msg,
                            translateX: 1200,
                            show: true,
                            translateY: this.createY()
                        })

                    }
                })
            },
            insert(temp) {
                if (!temp) {
                    temp = {
                        msg: this.barrage[this.currentIndex2].msg,
                        translateX: 1200,
                        show: true,
                        translateY: this.createY()
                    };
                }
                this.list.push(
                    temp
                )
                setTimeout(() => {
                    temp.translateX = -200
                }, 50)
                setTimeout(() => {
                    temp.show = false
                }, 8000)
            }
        },
        mounted() {
            // this.fetchBarrageBySeriesId()
            setInterval(() => {
                if (this.barrage &&
                    this.barrage[this.currentIndex2] &&
                    this.barrage[this.currentIndex2].time < this.currentTime
                ) {
                    this.currentIndex2++
                    this.insert()
                }
            }, 50)
        },

    }
</script>

<style>
  #wrapper {
    height: 400px;
    width: 700px;
    position: relative;
    overflow: hidden;
    background: url(http://www.drama-asia.se/wp-content/uploads/2016/06/14375197_1349947520504_800x600.jpg);

    color: #ffffff82;
    font-size: 14px;
    text-shadow: 1px 1px #000;
  }

  .move {
    transform: translateX(300px)
  }

  .barrage {
    position: absolute;
    white-space: nowrap;
    user-select: none;
    transition: transform 7s linear; /* 时间相同 越长的弹幕滑动距离越长 所以越快~ */
    transform: translateX(600px);
  }

</style>
