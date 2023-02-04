import Head from 'next/head'
import Image from 'next/image'
import styles from '@/styles/Home.module.css'

export default function Home() {
  return (
    <>
      <Head>
        <title>Markysparky</title>
        <meta name="description" content="HackSC '23 submission" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className="main">
        <div className="navbar">
          <div className="navbar--title">
            Markysparky
          </div>
          <div className='navbar--profile'>
            
          </div>
        </div>
        <div className="body">
          <div className="body--title">
            😁 Positive
          </div>
          <div className="body--card--row">
            <div className="body--card">
            <div className="body--card--title">
              Sample title
            </div>
            <div className="body--card--text">
              Lorem ipsum hello holy shit i wanna sleep i&apos;m so fuckin tired.
            </div>

            <div className="body--card--subtitle">
            😁 Positive
            </div>

            </div>

            <div className="body--card">

            <div className="body--card--title">
              Sample title
            </div>
            <div className="body--card--text">
              Lorem ipsum hello holy shit i wanna sleep i&apos;m so fuckin tired.
            </div>

            <div className="body--card--subtitle">
            😁 Positive
            </div>

            </div>
            <div className="body--card">

            <div className="body--card--title">
              Sample title
            </div>
            <div className="body--card--text">
              Lorem ipsum hello holy shit i wanna sleep i&apos;m so fuckin tired.
            </div>

            <div className="body--card--subtitle">
            😁 Positive
            </div>

            </div>
            <div className="body--card">

            <div className="body--card--title">
              Sample title
            </div>
            <div className="body--card--text">
              Lorem ipsum hello holy shit i wanna sleep i&apos;m so fuckin tired.
            </div>

            <div className="body--card--subtitle">
            😁 Positive
            </div>

            </div>
          </div>
          


        </div>
      </div>
    </>
  )
}
