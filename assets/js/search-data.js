// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-professional-service",
          title: "professional service",
          description: "summary of professional services including chairing, reviewing, and organization roles.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/service/";
          },
        },{id: "nav-awards",
          title: "awards",
          description: "recognitions and honors received.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/awards/";
          },
        },{id: "nav-grant",
          title: "grant",
          description: "externally funded research projects and fellowships.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/grants/";
          },
        },{id: "nav-talks",
          title: "talks",
          description: "invited and keynote talks at academic and professional venues.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/talks/";
          },
        },{id: "nav-teaching",
          title: "teaching",
          description: "courses taught and students co-supervised.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/teaching/";
          },
        },{id: "news-i-was-awarded-the-nih-pathway-to-independence-award-k99-r00",
          title: 'I was awarded the NIH Pathway to Independence Award (k99/R00)',
          description: "",
          section: "News",},{id: "news-four-papers-have-been-accepted-by-neurips-2024",
          title: 'Four papers have been accepted by NeurIPS 2024',
          description: "",
          section: "News",},{id: "news-served-as-the-acl-2025-area-chair",
          title: 'Served as the ACL 2025 Area Chair',
          description: "",
          section: "News",},{id: "news-our-me-llama-has-been-accepted-by-npj-digital-medicine",
          title: 'Our Me-LLaMA has been accepted by npj Digital Medicine',
          description: "",
          section: "News",},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%78%71%71.%73%69%6E%63%65%72%65@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/qianqian-xie-912571238", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=UYW7X_0AAAAJ# your Google Scholar ID", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
