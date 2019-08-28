<template>
<el-form ref="form" :model="form" label-width="80px">
		
	  <el-form-item label="真实姓名">
		<el-input v-model="form.name" placeholder="请填写真实姓名"></el-input>
	  </el-form-item>
	  
	  <el-form-item label="手机号码">
	  	<el-input v-model="form.phone" placeholder="请填写手机号码"></el-input>
	  </el-form-item>
	  
	  <el-form-item>
		<el-button type="primary" @click="onSubmit">提&nbsp;&nbsp;&nbsp;&nbsp;交</el-button>
	  </el-form-item>
</el-form>
</template>

<script>
	 export default {
    data() {
      return {
        form: {
          name: '',
          phone: '',
        }
      };
    },
    methods: {
      onSubmit() {
        console.log('submit!');
      }
    }
  }
</script>

<style scoped>
.el-form{
	margin:20px auto;
	width: 600px;
}
</style>
