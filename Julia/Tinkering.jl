using Makie

λ_slider = Makie.slider(0:.1:5, label="λ", raw = true, camera=campixel!, start=1.0);
μ_slider = Makie.slider(0:.1:5, label="μ", raw = true, camera = campixel!);
xs = range(0.0, 1.0, length = 100)

ys  = lift(λ_slider[end][:value], μ_slider[end][:value]) do λ, μ
    [ λ*x^2 + μ for x in xs]
end

plt = Makie.plot(xs, ys);
scene = Makie.hbox(plt, Makie.vbox(λ_slider, μ_slider), parent=Scene(resolution = (800, 800)))