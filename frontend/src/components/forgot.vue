<template>
  <div>
    <h1 style="text-align: center">找回密码</h1>
    <el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" label-width="100px" class="demo-ruleForm">

      <el-form-item label="用 户 名" prop="user">
        <el-input placeholder="请输入手机号" type="text" v-model="ruleForm2.user" auto-complete="off"></el-input>
      </el-form-item>

      <el-form-item label="邮    箱" prop="email">
        <el-input type="text" v-model="ruleForm2.email" placeholder="请输入邮箱地址">
          <el-button slot="append" :disabled="!send_email" @click="generate_email" id="mailbtn">发送验证码</el-button>
        </el-input>
      </el-form-item>

      <el-form-item label="验 证 码" prop="captcha">
        <el-input placeholder="输入邮件中的验证码" type="text" v-model="ruleForm2.captcha"></el-input>
      </el-form-item>

      <el-form-item label="新 密 码" prop="pass">
        <el-input placeholder="请输入新密码" type="password" v-model="ruleForm2.pass" auto-complete="off">
        </el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm2')" style="width: 220px;">重置密码</el-button>
      </el-form-item>

    </el-form>

    <div>
      <router-link :to="'/account/login'" tag="div" class="footer">去登陆</router-link>
      <router-link :to="'/account/register'" tag="div" class="footer">去注册</router-link>
    </div>

  </div>
</template>

<script>
  import util from '../utils/util.js'
  export default {
    name: 'forgot',
    data() {
      var validateuser = (rule, value, callback) => {
        console.log(value, /^\w{6,12}$/.test(value))
        if (value === '') {
          callback(new Error('请输入用户名'));
        } else if (!/^\w{6,12}$/.test(value)) {
          callback(new Error('用户名必须是6-12位数字字母下划线组成'));
        } else {
          callback()
        }

      };
      var validatepass = (rule, value, callback) => {
        console.log(value, /^.{6,12}$/.test(value))
        if (value === '') {
          callback(new Error('请输入新密码'));
        } else if (!/^.{6,12}$/.test(value)) {
          callback(new Error('密码必须是6-12位'));
        } else {
          callback()
        }

      };
      var validateemail = (rule, value, callback) => {
        console.log(value, /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/.test(value))
        if (value === '') {
          callback(new Error('请输入邮箱'));
        } else if (!/^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/.test(value)) {
          callback(new Error('请输入正确邮箱地址'));
        } else {
          callback()
        }

      };
      var validatecaptcha = (rule, value, callback) => {
        console.log(value, /^[a-zA-Z0-9]{4}$/.test(value))
        if (value === '') {
          callback(new Error('请输入验证码'));
        } else if (!/^[a-zA-Z0-9]{4}$/.test(value)) {
          callback(new Error('验证码必须是4位数字与字母'));
        } else {
          callback()
        }

      };
      return {
        pagename: 'login',
        email_url: '',
        ruleForm2: {
          user: '',
          pass: '',
          email: '',
          sendmail: false,
          uuid: '',
          captcha: '',

        },
        rules2: {
          user: [{
            validator: validateuser,
            trigger: 'blur'
          }],
          pass: [{
            validator: validatepass,
            trigger: 'blur'
          }],
          email: [{
            validator: validateemail,
            trigger: 'blur'
          }],
          captcha: [{
            validator: validatecaptcha,
            trigger: 'blur'
          }]
        },
        send_email: true,
      };
    },
    mounted() {
      var box = document.getElementsByClassName('login')[0];
      box.style.height = '500px';
    },
    methods: {
      generate_email() {
        this.$refs.ruleForm2.validateField('email', (value, valid) => {
          if (!valid) {
            this.send_email = false;
            console.log(this.host);
            this.ruleForm2.uuid = util.generate_uuid()
            this.email_url = this.host + '/email/' + this.ruleForm2.uuid + "/" + this.ruleForm2.email + "/";
            this.axios.get(this.email_url)
            this.ruleForm2.sendmail = true
            setTimeout(() => {
              this.send_email = true;
              console.log("send_email_btn", this.send_email);
            }, 3000);
          }
        });
        console.log(this.ruleForm2.uuid);
      },
      submitForm(formName) {
        console.log(this.ruleForm2.uuid);
        this.$refs[formName].validate((valid) => {
          if (!this.ruleForm2.sendmail) {
            this.$message({
              type: 'error',
              message: '未发送验证码邮件!'
            });
          }else if (valid) {
            this.axios.post(this.host + "/forgot/", {
              username: this.ruleForm2.user,
              password: this.ruleForm2.pass,
              email: this.ruleForm2.email,
              captcha: this.ruleForm2.captcha,
              uuid: this.ruleForm2.uuid
            }, {
              responseType: 'json',
              withCredentials: true,
            }).then(response => {
              console.log(response.statusText);
              this.pagename = 'info'
              this.$router.push({
                name: 'account'
              })
            }).catch(error => {
              this.$message({
                type: 'error',
                message: '密码重置失败!'
              });
            });
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },

    }
  }
</script>

<style>
  .footer {
    line-height: 50px;
    width: 49%;
    height: 50px;
    text-align: center;
    display: inline-block;
    color: #8A82DB;
    background: linear-gradient(#F0F8FF, white, #F0F8FF);
    font-size: 24px;

  }

  #mailbtn {
    padding: 10px;
  }

  .el-form {
    width: 400px;
    height: 300px;
    margin: 50px auto 40px auto;
    font-size: 16px;

  }

  .el-button img {
    width: 80px;

  }
</style>
