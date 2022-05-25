// API接口中心

import request from "@/api/request"

// 上传图片
export const reqUploadImage = ({data})=>request({
    url:"/upload",
    method: 'post',
    data: data
})

// 分页显示