// import Head from 'next/head'
// import Image from 'next/image'
// import styles from '@/styles/Home.module.css'
// import { OutputData } from "@editorjs/editorjs";
// import type { NextPage } from "next";
// import dynamic from "next/dynamic";
// import { useState } from "react";
// // important that we use dynamic loading here
// // editorjs should only be rendered on the client side.

// export default function Home() {
//   const EditorBlock = dynamic(() => import("../components/Editor"), {
//     ssr: false,
//   });
//   const Home: NextPage = () => {
//     //state to hold output data. we'll use this for rendering later
//     const [data, setData] = useState<OutputData>();
//   return (
//     <>
//       <Head>
//         <title>Markysparky</title>
//         <meta name="description" content="HackSC '23 submission" />
//         <meta name="viewport" content="width=device-width, initial-scale=1" />
//         <link rel="icon" href="/favicon.ico" />
//       </Head>
//       <div className="main">
//         <div className="navbar">
//           <div className="navbar--title">
//             Markysparky
//           </div>
//           <div className='navbar--profile'>
            
//           </div>
//         </div>
//         <div className="body">
//           <div className="body--title">
//             😁 Positive
//           </div>
//           <div className="body--card--row">
//             <div className="body--card">
//             <div className="body--card--title">
//               Sample title
//             </div>
//             <div className="body--card--text">
//               Lorem ipsum hello holy shit i wanna sleep i&apos;m so fuckin tired.
//             </div>

//             <div className="body--card--subtitle">
//             😁 Positive
//             </div>

//             </div>

//             <div className="body--card">

//             <div className="body--card--title">
//               Sample title
//             </div>
//             <div className="body--card--text">
//               Lorem ipsum hello holy shit i wanna sleep i&apos;m so fuckin tired.
//             </div>

//             <div className="body--card--subtitle">
//             😁 Positive
//             </div>

//             </div>
//             <div className="body--card">

//             <div className="body--card--title">
//               Sample title
//             </div>
//             <div className="body--card--text">
//               Lorem ipsum hello holy shit i wanna sleep i&apos;m so fuckin tired.
//             </div>

//             <div className="body--card--subtitle">
//             😁 Positive
//             </div>

//             </div>
//             <div className="body--card">

//             <div className="body--card--title">
//               Sample title
//             </div>
//             <div className="body--card--text">
//               Lorem ipsum hello holy shit i wanna sleep i&apos;m so fuckin tired.
//             </div>

//             <div className="body--card--subtitle">
//             😁 Positive
//             </div>

//             </div>
//           </div>

//         <EditorBlock data={data} onChange={setData} holder="editorjs-container" />

//         </div>
//       </div>
//     </>
//   )
// }
// }

import { OutputData } from "@editorjs/editorjs";
import type { NextPage } from "next";
import dynamic from "next/dynamic";
import { useState } from "react";
// important that we use dynamic loading here
// editorjs should only be rendered on the client side.
const EditorBlock = dynamic(() => import("../components/Editor"), {
  ssr: false,
});
const Home: NextPage = () => {
  //state to hold output data. we'll use this for rendering later
  const [data, setData] = useState<OutputData>();
  return (
    <EditorBlock data={data} onChange={setData} holder="editorjs-container" />
  );
};
export default Home;