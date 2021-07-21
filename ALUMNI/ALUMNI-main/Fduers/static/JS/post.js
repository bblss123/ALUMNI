var  replyThumb=0; //回贴：点赞
var  reactThumb=0; //主贴：点赞
var  reactCollect=0; //主贴：收藏

// 回贴：点赞
function reply_thumb()
{
//    reply_count = getReplyThumb();  从后端取数据

    replyThumb += 1;
    c = document.getElementById('replythumb');
    c.innerHTML = ' 赞 ' + replyThumb;
}

// 回贴：投诉
function complain()
{

}

// 主贴
function react_thumb()
{
    //    react_count = getReactThumb();  从后端取数据
    reactThumb += 1;
    var c1 = document.getElementById('reactthumb');
    c1.innerHTML = ' 赞 ' + reactThumb;
}

function react_collect()
{
    reactCollect += 1;
    var c2 = document.getElementById('reactcollect');
    c2.innerHTML = ' 收藏 ' + reactCollect;
}

// 回帖：只看楼主
function only_host()
{
}