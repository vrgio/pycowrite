# Nunc dapibus turpis odio

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas facilisis varius ex facilisis malesuada. Aliquam erat volutpat. Cras ultrices mauris tellus, vel vestibulum ante pretium id. Proin suscipit euismod lorem, sed dictum nunc consectetur in. Morbi a leo auctor tortor imperdiet rutrum.

Nunc dapibus turpis odio, vitae tincidunt turpis vestibulum ut. Nullam nec pellentesque dolor. Nam ullamcorper varius scelerisque. 
```
fn run_cache_subcommand(matches: &clap::ArgMatches) -> Result<()> {
    if matches.is_present("build") {
        #[cfg(feature = "build-assets")]
        build_assets(matches)?;
        #[cfg(not(feature = "build-assets"))]
        println!("bat has been built without the 'build-assets' feature. The 'cache --build' option is not available.");
    } else if matches.is_present("clear") {
        clear_assets();
    }

    Ok(())
}
```

> [bat - a cat(1) clone with wings](https://github.com/sharkdp/bat)

In dictum tincidunt eros, sit amet luctus odio lobortis a. Aliquam erat volutpat. Aliquam a justo at libero faucibus mollis in et libero.

