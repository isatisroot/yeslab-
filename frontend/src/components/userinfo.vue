<template>
  <div>
    <div class="infos" v-if="!empty" :model="infos">
      <div>
        <div class="infotitle">姓名</div>：
        <a>{{ infos.name }}</a>
      </div>
      <div>
        <div class="infotitle">手机</div>：
        <a>{{ infos.phone }}</a>
      </div>
      <div>
        <div class="infotitle">QQ</div>：
        <a>{{ infos.qq }}</a>
      </div>
      <div>
        <div class="infotitle">学校/企业</div>：
        <a>{{ infos.adress }}</a>
      </div>
    </div>
    <el-form ref="form" :model="form" label-width="110px" v-else-if="empty">

      <el-form-item label="真实姓名">
        <el-input v-model="form.name" placeholder="请填写真实姓名"></el-input>
      </el-form-item>

      <el-form-item label="手机号码">
        <el-input v-model="form.phone" placeholder="请填写手机号码"></el-input>
      </el-form-item>

      <el-form-item label="QQ">
        <el-input v-model="form.qq" placeholder="请填写QQ号码"></el-input>
      </el-form-item>

      <el-form-item label="学校/企业名称">
        <el-input v-model="form.adress" placeholder="请填写学校或企业名称"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">提&nbsp;&nbsp;&nbsp;&nbsp;交</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        userid:sessionStorage.user_id || localStorage.user_id,
        token:sessionStorage.token || localStorage.token,
        msg: '',
        form: {
          name: '',
          phone: '',
          qq: '',
          adress: ''
        },
        infos: {
          name: '',
          phone: '',
          qq: '',
          adress: ''
        },
        empty: '',
      };
    },
    mounted() {
      this.get_info();
    },
    methods: {
      onSubmit() {
        this.axios.post(this.host + "/userinfo/" + this.userid, {
          form: this.form
        }, {
          responseType: 'json',
          withCredentials: true,
        }).then(response => {
          this.$message({
            type: 'info',
            message: '提交成功!'
          });
          this.infos.name = this.form.name;
          this.infos.phone = this.form.phone;
          this.infos.qq = this.form.qq;
          this.infos.adress = this.form.adress;
          this.empty = false;
        })
        .catch(error => {
          console.log(error, "error");
          this.$message({
            type: 'error',
            message: error.response.data.msg + '提交失败!'
          });
          this.empty = true;
        });
      },
      get_info: function() {
        // 获取用户个人信息
        this.axios.get(this.host + '/userinfo/' + this.userid, {
          responseType: 'json',
          headers: {
            'Authorization': 'JWT ' + this.token
          },
          withCredentials: true, //跨域带上cookies
        }, ).then(response => {
          this.empty = response.data.empty
          if (!this.empty) {
            this.infos.name = response.data.name;
            this.infos.phone = response.data.phone;
            this.infos.qq = response.data.qq;
            this.infos.adress = response.data.adress;
          }else{
            this.$message({
              type: 'info',
              message: '请填写个人信息！',
            })
          }
        }).catch(error => {
          console.log(error.response.data);
        })
      },
    }
  }
</script>

<style scoped>
  .el-form {
    margin: 20px auto;
    width: 600px;
  }

  .infos{
    margin: 0 100px;
    color: darkcyan;
    line-height: 60px;
  }
  .infos a{
    color: black;
  }

  .infotitle{
    width: 80px;
    display: inline-block;
  }
</style>
