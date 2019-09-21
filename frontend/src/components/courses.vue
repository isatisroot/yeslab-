<template>
  <div>
    <el-page-header title="返回登录" @back="goBack" content="课程表"></el-page-header>
    <div class="course">
      <el-tabs type="border-card" @tab-click="get_courses">

        <el-tab-pane label="课表（日期表格）">
          课表（日期表格）
        </el-tab-pane>

        <el-tab-pane label="课表（开班通知表）">
          <el-table :data="courses">
            <el-table-column prop="name" label="课程名称" width="180"></el-table-column>
            <el-table-column prop="type" label="班型"></el-table-column>
            <el-table-column prop="teacher" label="上课老师"></el-table-column>
            <el-table-column prop="date" label="开课时间" width="180"></el-table-column>
            <el-table-column prop="time" label="上课时间"></el-table-column>
          </el-table>
        </el-tab-pane>

        <el-tab-pane label="高校活动表">
          高校活动表
        </el-tab-pane>

        <el-tab-pane label="讲师授课时间表">
          讲师授课时间表
        </el-tab-pane>

      </el-tabs>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        courses: [],
      };
    },
    methods: {
      get_courses: function(tab) {
        console.log();
        this.axios.get(this.host + '/course/' + tab.$data.index, {
          headers: {
            'Authorization': 'JWT ' + this.token
          },
          withCredentials: true, //跨域带上cookies
        }).then(response => {
          if (tab.$data.index == 1) {
            this.courses = response.data;
          }
        })
      },
      goBack: function(){
        this.$router.push({
          'name': 'account',
        })
      },
      choice: function(teacher){
        this.ischocie = true;
        this.teacher = teacher;
      }
    }
  }
</script>

<style>
  .course {
    width: 1200px;
    height: 600px;
    margin: 50px auto 0 auto;
    overflow: scroll;
  }

  .chocie{
    width: 1200px;
    padding: 20px;
    margin: 50px auto 0 auto;
    background-color: white;
    border: #ccc 1px solid;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .12), 0 0 6px 0 rgba(0, 0, 0, .04)
  }

  .maintable{
    overflow: scroll;
    text-align: center;
  }

  .tablecol{
    padding: 10px;
    border: #EEEEEE 1px solid;
  }

  .closechoice{
    cursor: pointer;
  }

  .el-main {
    color: #333;
  }

  body>.el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }

  ::-webkit-scrollbar {
    /*滚动条整体样式*/
    width: 6px;
    /*高宽分别对应横竖滚动条的尺寸*/
    height: 6px;
    background: #ffffff;
    cursor: pointer;

  }
  ::-webkit-scrollbar-thumb {
    /*滚动条里面小方块*/
    border-radius: 5px !important;
    -webkit-box-shadow: inset 0 0 5px rgba(240, 240, 240, .5) !important;
    ;
    background: #bea4fb;
    cursor: pointer !important;
  }
  ::-webkit-scrollbar-track {
    /*滚动条里面轨道*/
    background-color: #eee;
  }
</style>
