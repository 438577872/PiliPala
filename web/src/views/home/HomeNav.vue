<template>

  <el-row>


    <el-col :span="4" style="margin-top: 25px;border-right: 1px solid rgb(221,221,221)">
      <el-row :gutter="20" style="padding-left: 20px;padding-right: 20px">
        <el-col :span="6">
          <div style="border-radius: 50%;border: 0px solid black;display: block;"
               :style="{height:`${iconSize*2}px`,width:`${iconSize*2}px`,'line-height':`${iconSize*2.6}px`,background:'rgb(255,92,124)'}"
               align="center">
            <IconHome :size="iconSize+5" style="margin: auto"></IconHome>
          </div>
          <span style="margin-left: 10px;font-size: 10px">首页</span>
          <br>
        </el-col>



        <el-col :span="6">
          <div style="border-radius: 50%;border: 0px solid black;display: block;"
               :style="{height:`${iconSize*2}px`,width:`${iconSize*2}px`,'line-height':`${iconSize*2.6}px`,background:'rgb(252,186,42)'}"
               align="center">
            <IconDynamic :size="iconSize+5" style="margin: auto"></IconDynamic>
          </div>
          <span style="margin-left: 10px;font-size: 10px">动态</span>
          <br>
        </el-col>



        <el-col :span="6">
          <div style="border-radius: 50%;border: 0px solid black;display: block;"
               :style="{height:`${iconSize*2}px`,width:`${iconSize*2}px`,'line-height':`${iconSize*2.6}px`,background:'rgb(255,113,109)'}"
               align="center">
            <IconHot :size="iconSize+5" style="margin: auto"></IconHot>
          </div>
          <span style="margin-left: 10px;font-size: 10px">热门</span>
          <br>
        </el-col>



        <el-col :span="6">
          <div style="border-radius: 50%;border: 0px solid black;display: block;"
               :style="{height:`${iconSize*2}px`,width:`${iconSize*2}px`,'line-height':`${iconSize*2.6}px`,background:'rgb(109,199,129)'}"
               align="center">
            <IconChannel :size="iconSize+5" style="margin: auto"></IconChannel>
          </div>
          <span style="margin-left: 10px;font-size: 10px">频道</span>
          <br>
        </el-col>
      </el-row>
    </el-col>



    <el-col :span="16" style="padding-top: 20px;padding-bottom: 20px">
      <el-menu mode="horizontal" style="border-right: none;border-bottom: none;margin-top: 10px;;">
        <el-col :span="3" style="text-align: center;padding-top: 0px" :key="item.name" v-for="(item,index) in types">
          <el-popover
                  placement="top-start"
                  title="标题"
                  width="200"
                  trigger="hover"
                  content="这是一段内容,这是一段内容,这是一段内容,这是一段内容。">
            <div slot="reference">
              <div style="display: inline-block;width:80px;;cursor: pointer;margin-top: 5px;font-size: 10px">
                <span style="float: left">{{item.name}}</span>
                <font style="min-width: 25px;color: white;background: rgb(122,204,230);
                              border-radius: 3px;font-size: 0.01rem;float: left; margin-left: 5px">
                  {{item.val}}
                </font>
              </div>
            </div>
          </el-popover>
        </el-col>
      </el-menu>
    </el-col>
    <el-col :span="4" style=";margin-top: 20px;border-left: 1px solid rgb(221,221,221)">
      <el-col :span="8" v-for="item in actives" :key="item.name" style="text-align: center">
        <el-button type="text">
          {{item.name}}
        </el-button>
      </el-col>
    </el-col>
  </el-row>
</template>

<script>
    import IconHome from "@/components/icons/IconHome";
    import IconVoice from "@/components/icons/IconVoice";
    import HomeNav from "@/views/home/HomeNav";
    import IconHot from "@/components/icons/IconHot";
    import IconDynamic from "@/components/icons/IconDynamic";
    import IconChannel from "@/components/icons/IconChannel";

    export default {
        name: "HomeNav",
        components: {IconChannel, IconDynamic, IconHot, HomeNav, IconVoice, IconHome},
        props: [
            'iconSize',
            'actives',
            'types',

        ],
        data() {
            return {
                list: [
                    {
                        'name': '国产动画'
                    },
                    {
                        'name': '咨询'
                    },
                    {
                        'name': '国产动画'
                    },
                    {
                        'name': '官方延伸'
                    },
                    {
                        'name': '国产动画'
                    },
                    {
                        'name': '国产动画'
                    },
                ],
            }
        }

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
