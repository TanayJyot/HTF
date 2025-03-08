import React from 'react';
import guy from './data/Frame 55.webp'

const Hero2 = () => {
    return (
        <div className="relative flex justify-items-start">
            <img src={guy} alt="guy" className="w-full h-2/4"/>
            <div
                className="glass absolute rounded-2xl w-[650px] h-[382px] inset-y-24 flex items-center justify-center px-24 ml-12 backdrop-blur-sm">
                <div className="p-4">
                    <h6 className="text-justify font-analogist text-4xl text-[#FFF] font-normal tracking-wider pb-4">Meet the
                        Craftsman</h6>
                    <p className="font-josephin text-base leading-6 font-normal text-white text-justify"> Handloom
                        craftsmen, the unsung heroes of the textile industry, dedicate their lives to mastering the
                        ancient art of weaving, often beginning their training at a young age. With a deep understanding
                        of traditional techniques and an eye for intricate details, they create stunning fabrics that
                        showcase both their skill and cultural heritage. </p>
                </div>
            </div>
        </div>
    );
};

export default Hero2;
