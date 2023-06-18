<template>
    <div>
      <el-container class="container">
      <el-header>
        <el-row>
          <el-col :span="24">
            <h1 class="title">Environmental Uncertainty Perception Framework for Misinformation Detection and Spread Prediction</h1>
          </el-col>
        </el-row>
      </el-header>
  
      <el-table :data="newsList" class="table">
        <el-table-column label="Published Time" prop="date"></el-table-column>
        <el-table-column label="Content" width = 800>
          <template #default="{row}">
            {{ row.content }}
          </template>
        </el-table-column>
        <el-table-column label="Source" prop="source">
          <template #default="{row}">
            <el-tag>{{ row.source }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="Authenticity Label" prop="label">
          <template #default="{ row }">
            <el-tag :type="row.label === 'fake' ? 'danger' : 'success'">{{ row.label }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="Dissemination Label" prop="label_2">
          <template #default="{ row }">
            <el-tag :type="row.label_2 === 'high' ? 'danger' : 'success'">{{ row.label_2 }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column>
          <template #default="{ row }">
            <el-button @click="goToDetail(row.id)">more</el-button>
          </template>
        </el-table-column>
      </el-table>
        <el-pagination
          class="pagination"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[10, 20, 30, 50]"
          :page-size="pageSize"
          :total="total"
          layout="total, sizes, prev, pager, next, jumper"
        />

    </el-container>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
    export default {
      data() {
        return {
          newsList: [],
          currentPage: 1,
          pageSize: 10,
          total: 100
        }
      },
      created() {
        this.load();
      },
      methods: {
        goToDetail(id) {
          this.$router.push({ name: 'detail', params: { id: id }})
        },
        load() {
          axios.get('/api/getList', {
              params: {
                pageNum: this.currentPage,
                pageSize: this.pageSize
            }})
            .then(response => {
              if (response.data.code == 200) {
                console.log(response.data)
                this.newsList = response.data.data;
                this.total = response.data.total;
              }
            })
            .catch(error => {
              console.log(error);
            });
        },
        handleSizeChange(val) {
          this.pageSize = val;
          this.load();
        },
        handleCurrentChange(val) {
          this.currentPage = val;
          this.load();
        }
      },
    }
</script>

<style scoped>
.container {
  padding: 0 50px;
}
.title {
    margin-top: 20px;
    text-align: center;
}

.table {
    margin-top: 80px;
    margin-bottom: 50px;
}
</style>
