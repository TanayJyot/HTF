import React from 'react';
import hero from './data/image 3.webp'
import side from './data/image 4.webp'
import in1 from './data/DSC02137.webp'
import in2 from './data/IMG20230813150601.webp'
import in3 from './data/IMG20230814131836.webp'
import AboutUs from "../Homepage/AboutUs";


const About = () => {
    return (
        <div>
            {/*<img src={hero} alt="" className="w-full"/>*/}
            <div className="about-loomkar flex justify-center">
                <div className="mx-6">
                    <h3 className="font-analogist text-3xl text-justify text-[#656565] mt-24">About loomkar</h3>
                    <p className="font-josephin text-justify font-light leading-6 mt-4">Lorem ipsum dolor sit amet
                        consectetur. Enim vulputate eleifend pretium<br/> sagittis amet laoreet id.
                        Maecenas ac tincidunt lacinia dui in sagittis etiam<br/> neque morbi. Adipiscing arcu tincidunt
                        habitant integer porta iaculis congue.<br/> Sit consectetur penatibus cras varius turpis.</p>
                </div>
                <div>
                    <img src={side} alt="" className="mt-12"/>
                </div>
            </div>
            <div>
                <h2 className="font-analogist text-[2.5rem] leading-10 text-center mt-24 text-[#656565]"> Our Mission &
                    Vision</h2>
                <p className="font-josephin font-light leading-6 text-center mt-4 text-[#656565]"> At Loomkar, our
                    mission is to revive and sustain the timeless craft of
                    handloom weaving. We aim to empower artisans <br/>by providing them with fair wages, safe working
                    conditions, and the recognition they deserve. By connecting these <br/> master weavers with
                    contemporary
                    markets, we strive to create a sustainable ecosystem that benefits both the artisans<br/> and our
                    discerning customers.</p>
            </div>
            <div className="mt-32 w-full h-fit px-36 bg-[#F9F9F9]">
                <h3 className="pt-12 font-analogist text-[#656565] text-4xl"> What we offer </h3>
                <p className="text-justify font-josephin font-light mt-4"> Loomkar offers a curated collection of
                    handloom products that blend <br/>
                    traditional techniques with modern aesthetics. Our range includes:</p>
                <div className="mt-6 flex justify-start pb-36">
                    <div className="relative inline-block mr-4">
                        <img src={in1} alt="" className="block"/>
                        <div
                            className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-white px-7 py-9 text-center font-analogist leading-6 tracking-wide text-lg"
                            style={{background: "rgba(255, 255, 255, 0.26)"}}>Kurti's
                        </div>
                    </div>
                    <div className="relative inline-block mr-4">
                        <img src={in2} alt="" className="block"/>
                        <div
                            className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-white px-7 py-9 text-center font-analogist leading-8 text-lg"
                            style={{background: "rgba(255, 255, 255, 0.26)"}}>Hand bags
                        </div>
                    </div>
                    <div className="relative inline-block mr-4">
                        <img src={in3} alt="" className="block"/>
                        <div
                            className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-white px-7 py-9 text-center font-analogist leading-8 text-lg"
                            style={{background: "rgba(255, 255, 255, 0.26)"}}>Dupatta
                        </div>
                    </div>
                </div>
            </div>
            <div className="mb-24">
                <AboutUs/>
            </div>

        </div>
    );
};

export default About;
