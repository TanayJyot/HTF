import React from 'react';
import frame from './data/99b69ecc2590a3581cdd4f2b946826b0.webp'

const HeroCard = () => {
    return (
        <div className="hero-card relative flex justify-center">
            <img src={frame} alt="" className=" h-[550px] w-screen"/>
            <div className="glass absolute rounded-2xl w-[840px] h-[400px] inset-y-24 flex items-center justify-center px-36 backdrop-blur-md">
                <div className="p-4">
                    <h6 className="text-center font-analogist text-4xl text-[#FFF] font-normal tracking-wider">Handloom
                        Products</h6>
                    <hr className="mb-6 mt-4"/>
                    <p className="font-josephin text-base leading-6 font-normal text-white text-center">Handloom products,
                        celebrated for their intricate craftsmanship and cultural heritage, exemplify
                        the rich traditions and skilled artistry passed down through generations. These handmade
                        textiles, ranging from vibrant sarees and shawls to exquisite carpets and tapestries, are
                        not
                        only a testament to the weaver's dedication and expertise but also a symbol of sustainable
                        and
                        ethical fashion. </p>
                </div>
            </div>
        </div>
    );
};

export default HeroCard;
