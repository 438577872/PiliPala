<template>
  <div>
    <el-col :span="6" v-for="item in list" :key="item.index_picture_url">
      <div style=";padding: 20px;height: 200px">
        <el-link :underline="false" @click="to(item)">
          <el-image style="width:100%;height: 120px" fit="cover" :src="'/static/image/'+item.index_picture_url">
          </el-image>
          {{item.title}}
        </el-link>
      </div>
    </el-col>
  </div>
</template>

<script>
    import {findAllVideoByPage} from "@/api/UserApi";
    import {mapGetters} from "vuex";

    export default {
        name: "SpaceVideoList",
        computed: {
            ...mapGetters([
                'avatar', 'up_id'
            ])
        },
        data() {
            return {
                list: null,
            }
        },
        methods: {
            init() {
                findAllVideoByPage(this.up_id).then(resp => {
                    this.list = resp.data
                    this.finishLoading()
                })
            },
            to(item) {
                this.$router.push({
                    path: '/video',
                    query: {
                        series_id: item.id

                    }
                })
            },
            finishLoading() {
                this.$emit('finishLoading')
            }
        },
        mounted() {
            this.init()
        }
    }
</script>

<style scoped>

</style>
