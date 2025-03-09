import logo from './logo.svg';
import './App.css';
import Navbar from '../Navbar';
import Navbar2 from "./Navbar2";
import HeroCarousel from "./HeroCarousel";
import Grids from "./Grids";
import HeroCard from "./HeroCard";
import Hero2 from "./Hero2";
import AboutUs from "./AboutUs";
import PreFooter from "./PreFooter";




function Home() {
    return (
        <div className="App">
            
            <h3 className="font-analogist text-4xl mx-5"> Our featured products</h3>
            <p className="text-base font-josephin mb-16 mx-5"> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut
                consequuntur
                deserunt dolores, </p>
            <Grids second={false} />
            <HeroCard/>
            <h3 className="font-analogist text-4xl pt-10 tracking-widest font-normal mx-5"> Our kurti collections</h3>
            <p className="font-josephin text-base font-light px-96 leading-6  text-[#656565] pt-2.5 pb-30 mx-5">Lorem ipsum dolor sit amet consectetur. Dui dui orci turpis mi at tempor nisl <br/>    ullamcorper
                etiam.</p>
            <Grids second={true} />
            <Hero2 />
            <AboutUs />
            <PreFooter />

        </div>
    );
}

export default Home;
