import React from 'react';
import logo from './Homepage/data/image 1.png';

const Footer = () => {
    return (
        <footer className="p-10 bg-[#2B2B2B] text-base-content flex flex-col justify-around">
            <img src={logo} alt="" className="bg-white mb-4 w-32 ml-24"/>
            <div className="flex justify-around">
            <div className="flex flex-col items-start">

                <p className="text-[#F5F5F5] leading-6 font-josephin text-justify font-light">Lorem ipsum dolor sit amet
                    consectetur. Tempor est <br/> pellentesque lectus scelerisque cursus
                    sollicitudin. Arcu urna in <br/>at semper posuere in vitae malesuada maecenas. Lobortis <br/> purus
                    vulputate
                    augue euismod cras semper nibh in tristique.<br/> Volutpat donec dictum in vitae nisi mattis.</p>
            </div>
            <nav className="flex flex-col">
                <h6 className="font-analogist text-justify text-[#F5F5F5] leading-6 tracking-[0.005em]">Products</h6>
                <a className="link link-hover text-white font-light font-josephin leading-6 text-justify">Kurtis</a>
                <a className="link link-hover text-white font-light font-josephin leading-6 text-justify">Sarees</a>
            </nav>
            <nav className="flex flex-col">
                <h6 className="font-analogist text-justify text-[#F5F5F5] leading-6 tracking-[0.005em]">Important
                    Links</h6>
                <a className="link link-hover text-white font-light font-josephin leading-6 text-justify">Home</a>
                <a className="link link-hover text-white font-light font-josephin leading-6 text-justify">Products</a>
                <a className="link link-hover text-white font-light font-josephin leading-6 text-justify">About Us</a>
                <a className="link link-hover text-white font-light font-josephin leading-6 text-justify">Contact Us</a>
            </nav>
            <nav className="flex flex-col">
                <h6 className="font-analogist text-justify text-[#F5F5F5] leading-6 tracking-[0.005em]">Products</h6>
                <p className="text-[#F5F5F5] leading-6 font-josephin text-justify font-light">Shop no. 359-B, Beside
                    natural <br/> ice creams, Samta Colony,<br/> Raipur (C.G)</p>

            </nav>
                </div>
        </footer>
    )
        ;
};

export default Footer;
