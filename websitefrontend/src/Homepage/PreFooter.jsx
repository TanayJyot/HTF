import React from 'react';
import truck from './data/truck-fast.svg'
import money from './data/money.svg'
import headphone from './data/headphone.svg'
import wand from './data/magicpen.svg'

const PreFooter = () => {
    return (
        <div className="mt-10 flex justify-center text-center bg-[#F4F4F4] w-full p-7 gap-14 h-full">
            <div className="flex flex-col justify-center items-center mr-14">
                <img src={truck} alt="" className="w-6"/>
                <p className="text-[#2B2B2B] text-justify text-base font-semibold font-josephin">Free Shipping</p>
            </div>
   <div className="flex flex-col justify-center items-center mr-14">
                <img src={headphone} alt="" className="w-6"/>
                <p className="text-[#2B2B2B] text-justify text-base font-semibold font-josephin">Dedicated Support</p>
            </div>
   <div className="flex flex-col justify-center items-center mr-14">
                <img src={wand} alt="" className="w-6"/>
                <p className="text-[#2B2B2B] text-justify text-base font-semibold font-josephin">Cultural Heritage</p>
            </div>
   <div className="flex flex-col justify-center items-center mr-14">
                <img src={money} alt="" className="w-6"/>
                <p className="text-[#2B2B2B] text-justify text-base font-semibold font-josephin">Cash On Delivery</p>
            </div>

        </div>
    );
};

export default PreFooter;
