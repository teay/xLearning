for counter in 1 2 3 4 5; do
    echo $counter
done

for counter in {1..5}; do
    echo $counter
done

for counter in {1..10..2}; do
    echo $counter
done

for counter in {1..10..-2}; do
    echo $counter
done

for counter in {5..0..-1}; do
    echo $counter
    sleep 0.5s
    echo '----'
done
echo 'take off ^^^^^'

for i in {1..12}; do
    m=$((2*i))
    echo "2 x ${i} = ${m}"
done

n=12
for i in {1..12}; do
    m=$((n*i))
    # echo "${n} x ${i} = ${m}"
    printf "%3d x %3d = %3d\n" $n $i $m
done

for f in lily carnation 'for get me not' tulip; do
    echo $f
done

flowers=(lily carnation 'for get me not' tulip)
for f in "${flowers[@]}"; do
    echo $f
done

for f in cats.txt dogs.txt flower.txt; do
    head -n2 "$f"
    echo '----------'
done

url="https://assets.pokemon.com/assets/cms2/img/pokedex/full/"
for i in $(cat get_them.txt); do
    echo $i
    s="${i}.png"
    curl -O "${url}${s}"
done

for i in $(cat get_them.txt); do
    echo $i
    f="${i}.png"
    ffmpeg -i "$f" "${f%png}webp"
done

for f in *.png; do
    ffmpeg -i "$f" -vf format=gray "gray_$f"
done

for suit in S H D C; do
    for rank in A 2 3 4 5 6 7 8 9 10 J Q K; do
    echo -n "${rank}${suit} "
    done
done

