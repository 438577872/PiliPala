<template>
  <el-row :gutter="15" style="margin-top: 20px">
    <el-col :span="16">
      <el-card>
        <div>
          <el-row>
            <SpaceHomeMyVideo></SpaceHomeMyVideo>
          </el-row>
          <el-divider></el-divider>
        </div>
        <div>
          <el-row>
            <el-col :span="4"><h3>我的专栏</h3></el-col>
            <!--            <el-col :offset="4" :span="8"><span style="color: rgb(203,208,216)">还没有上传过视频哦~</span> <span class="primary">立即上传</span>-->
            <!--            </el-col>-->
          </el-row>
          <el-divider></el-divider>
        </div>
        <div>
          <el-row>
            <el-col :span="4"><h3>我的频道</h3></el-col>

            <!--            <el-col :offset="4" :span="8"><span style="color: rgb(203,208,216)">还没有上传过视频哦~</span> <span class="primary">立即上传</span>-->
            <!--            </el-col>-->
          </el-row>
          <el-row>
            <el-col align="center">
              <div style=";margin-left: auto;margin-right: auto">
                <span class="font-dark-gray" style="font-size: 12px;">投稿视频可以分类展示了</span> <br>
                <el-button type="primary" style="color: white;width: 130px;margin-top: 20px ">创建频道</el-button>
              </div>
            </el-col>
          </el-row>
          <el-divider></el-divider>
        </div>

      </el-card>
    </el-col>
    <el-col :span="8">
      <el-card style="text-align: center">
        <b>点击申请 BiliBili 认证</b>
        <br>
        获得 bilibili 认证，享受多重认证福利！

      </el-card>
      <el-card style="text-align: center;margin-top: 20px">
        创作中心
        <br>
        <el-button-group>
          <el-button>视频投稿</el-button>
          <el-button>内容管理</el-button>
        </el-button-group>
      </el-card>
      <el-card style=";margin-top: 20px">
        <template slot="header">
          公告
        </template>
        <el-input placeholder="编辑我的公告">

        </el-input>
      </el-card>
    </el-col>

  </el-row>
</template>

<script>
    import SpaceHomeMyVideo from "@/views/space/components/SpaceHomeMyVideo";

    export default {
        name: "SpaceHome",
        components: {SpaceHomeMyVideo},
        data(){
            return{
                args:this.$route.params
            }
        }
    }
</script>

<style scoped>

</style>
