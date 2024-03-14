<template>
    <div className="stats_wrapper flex">
        <div className="stats_item">
            <div className="stats_item_qol flex">
                <div className="item_qol">
                    7.4
                </div>
            </div>
            <div className="stats_descr">
                The best region
            </div>
            <div className="stats_title">
                Arkhangelsk
            </div>
            <div className="stats_hist flex">
                <div className="stats_hist_img"><img src="../assets/img/uparrow.svg" alt=""></div>
                <div className="stats_hist_text">
                    1.7 Compared to last quarter
                </div>
            </div>
        </div>
        <div className="stats_item">
            <div className="stats_item_qol flex">
                <div className="item_qol">
                    7.4
                </div>
            </div>
            <div className="stats_descr">
                The best category
            </div>
            <div className="stats_title">
                Safety
            </div>
            <div className="stats_hist flex">
                <div className="stats_hist_img"><img src="../assets/img/uparrow.svg" alt=""></div>
                <div className="stats_hist_text">
                    1.2 Compared to last quarter
                </div>
            </div>
        </div>
        <div className="stats_item">
            <div className="stats_item_qol flex">
                <div className="item_qol">
                    1.5
                </div>
            </div>
            <div className="stats_descr">
                The worst category
            </div>
            <div className="stats_title">
                Tourism
            </div>
            <div className="stats_hist flex">
                <div className="stats_hist_img"><img src="../assets/img/downarrow.svg" alt=""></div>
                <div className="stats_hist_text">
                    0.3 Compared to last quarter
                </div>
            </div>
        </div>
        <div className="stats_item">
            <div className="stats_item_qol flex">
                <div className="item_qol">
                    <img src="../assets/img/Subtract.svg" alt="">
                </div>
            </div>
            <div className="stats_descr">
                Data collected
            </div>
            <div className="stats_title">
                2040
            </div>
            <div className="stats_hist flex">
                <div className="stats_hist_img"><img src="../assets/img/uparrow.svg" alt=""></div>
                <div className="stats_hist_text">
                    1058 Compared to last quarter
                </div>
            </div>
        </div>
    </div>
</template>

<script>


</script>

<style scoped>
.stats_wrapper {
    width: 100%;
    justify-content: space-between;
    margin-bottom: 30px;
}
.stats_item {
    position: relative;
    padding: 16px;
    width: 300px;
    border-radius: 15px;
    background: #fff;
    box-shadow: 6px 6px 54px 0px rgba(0, 0, 0, 0.05);
}
.stats_item_qol {
    width: 60px;
    height: 60px;
    position: absolute;
    border-radius: 23px;
    background-color: #D9F7E7;
    right: 16px;
    align-items: center;
    justify-content: center;
}
.item_qol {
    font-weight: 700;
    font-size: 28px;
    color: #4AD991;
}
.stats_descr {
    margin-bottom: 16px;
    font-size: 16px;
    font-weight: 500;
}
.stats_title {
    margin-bottom: 12px;
    font-size: 28px;
    font-weight: 700;
}
.stats_hist {
    align-items: center;
}
.stats_hist_img {
    margin-right: 5px;
}
.stats_hist_text{
    font-weight: 500;
    font-size: 16px;
}
</style>