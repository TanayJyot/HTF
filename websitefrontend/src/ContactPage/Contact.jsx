import React from 'react';
import telephones from './data/image 3.png'

const Contact = () => {
    return (
        <div className="mb-48">
            <img src={telephones} alt="" className="w-full mb-4"/>
            <div className="mx-24 mt-12">
                <h3 className="font-analogist text-4xl"> Contact us </h3>
                <p className="font-josephin text-[#656565] font-light"> Lorem ipsum dolor sit amet consectetur.
                    Dignissim curabitur diam quis leo commodo ultrices
                    . Netus aliquam <br/> suspendisse suspendisse et commodo nullam tristique nunc aenean.</p>
            {/*    <form className="mt-4">*/}
            {/*        <input type="text" placeholder="name"*/}
            {/*               className="input input-bordered input-md w-full max-w-xs font-josephin font-semibold mr-4 rounded-none"/>*/}
            {/*        <input type="text" placeholder="email"*/}
            {/*               className="input input-bordered input-md w-full max-w-xs font-josephin font-semibold rounded-none"/>*/}
            {/*        <textarea placeholder="message"*/}
            {/*                  className="textarea textarea-bordered textarea-md w-full max-w-xs block rounded-none mt-4*/}
            {/*                   font-josephin font-semibold"/>*/}
            {/*    </form>*/}
            {/*</div>*/}
            <div className="container mx-auto py-4">
                <form>
                    <div className="flex flex-col mb-4">
                        <div className="w-full md:w-1/2 mb-4 md:mb-0 flex">
                            <input
                                type="text"
                                placeholder="name"
                                className="input input-bordered input-md w-full max-w-xs font-josephin font-semibold mr-4 rounded-none"
                            />
                            <input
                                type="email"
                                placeholder="email"
                                className="input input-bordered input-md w-full max-w-xs font-josephin font-semibold rounded-none"
                            />
                        </div>
                        <div className="">
            <textarea
                placeholder="message"
                className="textarea textarea-bordered textarea-md w-full block rounded-none mt-4 font-josephin font-semibold"/>
                        </div>
                    </div>
                    <button className="btn-md bg-black text-white font-josephin text-center px-10"> Submit </button>
                </form>
            </div>
        </div>
            </div>
    );
};

export default Contact;
