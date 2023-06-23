<template>
    <div>
        <el-descriptions title="Post Information" direction="vertical" :column="4" class="container">
          <el-descriptions-item label="Published_time">{{this.date}}</el-descriptions-item>
          <el-descriptions-item label="Source">
              <el-tag >{{ this.source }}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="label">
              <el-tag type="danger">{{ this.label }}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="spread label">
              <el-tag type="danger">{{ this.label_2 }}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="Content" span=4>{{ this.content }}
          </el-descriptions-item>
          
          <el-descriptions-item label="Macro media environment" :span="4">
              <el-table
                  :data="macro"
                  style="width: 100%">
                  <el-table-column
                      prop="date"
                      label="date"
                      width="180">
                  </el-table-column>
                  <el-table-column
                      prop="content"
                      label="content">
                  </el-table-column>
              </el-table>
          </el-descriptions-item>
          <el-descriptions-item label="Micro conmunicative environment" :span="4">
              <el-table
                  :data="micro"
                  style="width: 100%">
                  <el-table-column
                      prop="date"
                      label="date"
                      width="180">
                  </el-table-column>
                  <el-table-column
                      prop="content"
                      label="content">
                  </el-table-column>
              </el-table>
          </el-descriptions-item>
          
          <el-descriptions-item label="Uncertainty Analysis" span="4">
              <el-row>
                  <el-col :span="3">
                      <el-progress type="circle" :percentage="unc" :status="unc > 50 ? 'warning' : 'success'"></el-progress>
                  </el-col>
                  <el-col :span="3">
                    <div class="statistic-card">
                      <el-statistic :value=cases>
                        <template #title>
                          <div style="display: inline-flex; align-items: center">
                            Daily number of cases
                            <el-tooltip
                              effect="dark"
                              content="Number of users who logged into the product in one day"
                              placement="top"
                            >
                              <el-icon style="margin-left: 4px" :size="12">
                                <Warning />
                              </el-icon>
                            </el-tooltip>
                          </div>
                        </template>
                      </el-statistic>
                      <div class="statistic-footer">
                        <div class="footer-item">
                          <span>than yesterday</span>
                          <span :class="percent[0] === '-' ? 'green' : 'red'">
                            {{this.percent}}
                            <el-icon>
                              <CaretTop />
                            </el-icon>
                          </span>
                        </div>
                      </div>
                    </div>
                  </el-col>

                    <el-col :span="12" style="margin-top: 15px;">
                      <el-row>
                          <el-col :span="12">
                              macro-media environment uncertainty:
                          </el-col>
                          <el-col :span="6">
                            <el-progress :percentage="macro_unc" :format="format" :status="macro_unc > 60 ? 'warning' : 'success'"></el-progress>
                          </el-col>
                      </el-row>
                      <el-row>
                          <el-col :span="12">
                              micro-communicative environment uncertainty:
                          </el-col>
                          <el-col :span="6">
                            <el-progress :percentage="micro_unc" :format="format" :status="micro_unc > 60 ? 'warning' : 'success'"></el-progress>
                          </el-col>
                      </el-row>
                      <el-row>
                          <el-col :span="12">
                              physical environment uncertainty:
                          </el-col>
                          <el-col :span="6">
                            <el-progress :percentage="physical_unc" :format="format" :status="physical_unc > 60 ? 'warning' : 'success'"></el-progress>
                          </el-col>
                      </el-row>
                      <el-row>
                          <el-col :span="12">
                              message-framing uncertainty:
                          </el-col>
                          <el-col :span="6">
                            <el-progress :percentage="content_unc" :format="format" :status="content_unc > 60 ? 'warning' : 'success'"></el-progress>
                          </el-col>
                      </el-row>
                  </el-col>
              </el-row>
              
          </el-descriptions-item>
      </el-descriptions>
      <div class="center">
        <el-button type="primary"  @click="goBack">Back</el-button>
      </div>
      <div class="filler"></div>
    </div>
  </template>


<script>
import axios from 'axios';
export default {
  data() {
    return {
      id: '1',
      date: '',
      source: '',
      label: '',
      label_2: '',
      content: '',
      macro: [],
      micro: [],
      macro_unc: 0,
      micro_unc: 0,
      content_unc: 0,
      physical_unc: 0,
      unc: 0,
      percent: '',
      cases: 0
    }
  },
  created() {
    this.load();
  },
  methods: {
    load(){
      console.log(this.$route.params.id)
      axios.get('/api/getDetail', {
          params: {
            id: this.$route.params.id
        }})
        .then(response => {
          if (response.data.code == 200) {
            console.log(response.data)
            this.id = this.$route.params.id,
            this.date = response.data.data.date,
            this.source = response.data.data.source,
            this.label = response.data.data.label,
            this.label_2 = response.data.data.label_2,
            this.content = response.data.data.content,
            this.macro = response.data.data.macro,
            this.micro = response.data.data.micro
            this.macro_unc = response.data.data.macro_unc;
            this.micro_unc = response.data.data.micro_unc;
            this.content_unc = response.data.data.content_unc;
            this.physical_unc = response.data.data.physical_unc;
            this.unc = (response.data.data.macro_unc + response.data.data.micro_unc + response.data.data.physical_unc + response.data.data.content_unc)/4
            this.percent = response.data.data.percent;
            this.cases = response.data.data.cases
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    goBack() {
        this.$router.go(-1); // 返回前一页
    }
  }
}
</script>

<style scoped>
.container {
  margin-top: 40px;
  padding: 0 20px;
}

.container {
  display: flex;
  flex-direction: column;
  height: 100%;
}


.center {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.filler {
  flex: 1;
}

.el-descriptions__label {
  font-weight: bold !important;
}

.statistic-card {
  height: 100%;
  padding: 20px;
  border-radius: 4px;
  background-color: var(--el-bg-color-overlay);
}

.statistic-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  font-size: 12px;
  color: var(--el-text-color-regular);
  margin-top: 16px;
}

.statistic-footer .footer-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.statistic-footer .footer-item span:last-child {
  display: inline-flex;
  align-items: center;
  margin-left: 4px;
}

.green {
  color: var(--el-color-success);
}
.red {
  color: var(--el-color-error);
}


</style>