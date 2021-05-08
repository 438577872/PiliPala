<template>
  <div style="height: 600px">
    <el-row>
      <el-col :span="18">
        <el-form label-position="right" label-width="80px">
          <el-form-item label="标题">
            <el-input v-model="form.title" placeholder="请编辑你的标题" style="width: 80%">
            </el-input>
          </el-form-item>
          <el-form-item label="视频类型">
            <el-select v-model="form.type" placeholder="请选择类型">
              <el-option
                      v-for="item in options"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value"
                      :disabled="item.disabled">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            请在右边先选择一张图片作为视频的封面
          </el-form-item>
          <el-form-item>
            <el-upload
                    style="width: 50%;"
                    class="upload-demo"
                    ref="upload"
                    action="/api/file/uploadVideo"
                    :headers="{token:getToken()}"
                    :on-preview="handlePreview"
                    :data="form2"
                    :on-remove="handleRemove"
                    :file-list="fileList"
                    :multiple="true"
                    :auto-upload="false"
            >
              <el-button slot="trigger" size="small" type="primary" style="color: white">从本地选择视频</el-button>
              <el-button style="margin-left: 10px;color: white;background: rgb(251,114,153);" size="small"
                         @click="submitUpload">
                点击投稿
              </el-button>
            </el-upload>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="6">
        <el-upload
                class="avatar-uploader"
                action="/api/file/uploadIndexImage"
                :show-file-list="false"
                :headers="{token:getToken()}"
                :data="form"
                :on-success="handleAvatarSuccess"
                :before-upload="beforeAvatarUpload">
          <img v-if="imageUrl" :src="imageUrl" class="avatar">
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-col>
      {{form2}}
    </el-row>

  </div>
</template>

<script>
    import {getToken} from "@/utils/auth";

    export default {
        name: "SpaceUploadDialog",
        data() {
            return {
                fileList: [],
                formDataList: {},
                options: [
                    {
                        value: 'animation',
                        label: '动画'
                    },
                    {
                        value: 'movie',
                        label: '音乐',
                    },
                    {
                        value: 'dance',
                        label: '舞蹈'
                    },
                    {
                        value: 'knowledge',
                        label: '知识'
                    },
                    {
                        value: 'life',
                        label: '生活'
                    },
                    {
                        value: 'fashion',
                        label: '时尚'
                    },
                    {
                        value: 'enjoy',
                        label: '娱乐'
                    },
                    {
                        value: 'game',
                        label: '游戏'
                    },
                    {
                        value: 'data',
                        label: '数码'
                    },
                    {
                        value: 'ghost',
                        label: '鬼畜'
                    },
                    {
                        value: 'information',
                        label: '资讯'
                    }
                ],
                form: {
                    type: '',
                    title: '',
                },
                imageUrl: '',
                form2: {},
                getToken
            }
        },
        methods: {
            handleAvatarSuccess(res, file) {
                this.imageUrl = URL.createObjectURL(file.raw);
                this.form2 = res.data
                this.form2.up_id = this.$route.params.id
                // console.log(res.data)
                // for (let key in res.data){
                //     this.form2[key] = res.data[key]
                // }
            },
            beforeAvatarUpload(file) {
                const isJPG = file.type === 'image/jpeg';
                const isLt2M = file.size / 1024 / 1024 < 5;

                if (!isJPG) {
                    this.$message.error('上传头像图片只能是 JPG 格式!');
                }
                if (!isLt2M) {
                    this.$message.error('上传头像图片大小不能超过 2MB!');
                }
                return isJPG && isLt2M;
            },
            submitUpload() {
                this.$refs.upload.submit();
            },
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            handlePreview(file) {

            },
            commit(file) {
                this.$refs.upload.submit();
            }
        }

    }
</script>

<style scoped>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }

  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }

  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }

  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>
