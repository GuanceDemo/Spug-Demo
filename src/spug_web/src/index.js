/**
 * Copyright (c) OpenSpug Organization. https://github.com/openspug/spug
 * Copyright (c) <spug.dev@gmail.com>
 * Released under the AGPL-3.0 License.
 */
import React from 'react';
import ReactDOM from 'react-dom';
import { Router } from 'react-router-dom';
import { ConfigProvider } from 'antd';
import zhCN from 'antd/es/locale/zh_CN';
import './index.less';
import App from './App';
import moment from 'moment';
import 'moment/locale/zh-cn';
import * as serviceWorker from './serviceWorker';
import { history, updatePermissions } from 'libs';
import { datafluxRum } from '@cloudcare/browser-rum';

const datakitOrigin = process.env.DATAKIT_ORIGIN;
const rum_env = process.env.RUM_ENV;
const rum_version = process.env.RUM_VERSION;
const rum_service = process.env.RUM_SERVICE;
const sessionSampleRate = process.env.SESSION_SAMPLE_RATE;
const sessionReplaySampleRate = process.env.SESSION_REPLAY_SAMPLE_RATE;
const trackInteractions = process.env.TRACK_INTERACTIONS;
const traceType = process.env.TRACE_TYPE;

datafluxRum.init({
    applicationId: 'spug_web',
    datakitOrigin: 'http://47.106.191.26:9529',// datakitOrigin,
    env: 'dev' , //rum_env,
    version: '1.0',//rum_version,
    service: 'spug-web', //rum_service,
    sessionSampleRate: 100, //sessionSampleRate,
    sessionReplaySampleRate: 100,//sessionReplaySampleRate,
    trackInteractions: true,
    traceType: traceType, // 非必填，默认为ddtrace，目前支持 ddtrace、zipkin、skywalking_v3、jaeger、zipkin_single_header、w3c_traceparent 6种类型
    allowedTracingOrigins: [/.*/],  // 非必填，允许注入trace采集器所需header头部的所有请求列表。可以是请求的origin，也可以是是正则
})
datafluxRum.startSessionReplayRecording();

moment.locale('zh-cn');
updatePermissions();

ReactDOM.render(
  <Router history={history}>
    <ConfigProvider locale={zhCN} getPopupContainer={() => document.fullscreenElement || document.body}>
      <App/>
    </ConfigProvider>
  </Router>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
