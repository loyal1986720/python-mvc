#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Core.DecorateFunc import get, post
from  App.Core.BaseController import BaseController
from App.Library.Result import Result
from App.Models.DiagModel import DiagModel
import time, asyncio


class IndexController(BaseController):

    dg = None
  #  middlewares = ['checkLogin']
    def __init__(self):
        self.dg = DiagModel()

    # 首页文章列表
    @get('/')
    def index(self):
        data = {}
        #data['articleList'] = self.dg.articleList()
        return Result().setCode(Result.CODE_SUCCESS).setData(data).setMsg('操作成功').toJson()

    # 文章详情页
    @get('/article/{id}')
    async def article(self, id):
        print('article')
        data = self.dg.article(id)
        if data == None:
            return Result().setCode(Result.CODE_ERROR).setMsg('无此文章').toJson()
        else:
            return Result().setCode(Result.CODE_SUCCESS).setData(data).setMsg('操作成功').toJson()

    # 服务套餐列表
    @get('/service')
    async def service(self):
        print('service')
        data = {}
        await asyncio.sleep(3)
        data['serviceList'] = await self.dg.service()
        return Result().setCode(Result.CODE_SUCCESS).setData(data).setMsg('操作成功').toJson()

    # 上传照片
    @post('/sendDiag')
    def sendDiag(self, **kw):
        return Result().setCode(Result.CODE_SUCCESS).setMsg('操作成功').toJson()

    # 支付某次罐诊
    @post('/payDiag')
    def payDiag(self):
        pass

    # 我的记录
    @get('/diagRecord')
    def diagRecord(self):
        pass

    # 我已购买的服务
    @get('/myService')
    def myService(self):
        pass