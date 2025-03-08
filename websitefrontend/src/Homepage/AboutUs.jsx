import React from 'react';
import founder from './data/DSC02213 1.webp';  // Adjust the path to your image

const AboutUs = () => {
    return (
        <div className="About flex justify-center mx-5">
            <div className="shadow-xl w-[80%] mt-12 bg-[#F4F4F4] flex flex-col md:flex-row rounded-none p-7">
                <div className="flex justify-center md:w-1/2">
                    <figure>
                        <img src={founder} alt="Founder" className="w-full md:w-96"/>
                    </figure>
                </div>
                <div className="flex flex-col justify-center md:w-1/2">
                    <h2 className="card-title font-analogist leading-10 text-4xl tracking-[1.55px] font-normal">
                        Meet the owner
                    </h2>
                    <p className="font-josephin leading-6 font-light text-justify mt-4">
                        Welcome to our handloom clothing haven! I'm Sonia Singh, the proud owner and passionate curator
                        of this unique collection. Growing up, I was surrounded by the vibrant colors and intricate
                        patterns of handwoven fabrics, which sparked my lifelong love for these timeless treasures.
                        Inspired by the skilled artisans who dedicate their lives to perfecting this ancient craft, I
                        established this platform to celebrate their artistry and provide them with the recognition they
                        deserve.
                    </p>
                    <div className="mt-4 flex justify-start">
                        <button className="btn rounded-none bg-[#292D32] text-white w-36">About us</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AboutUs;
