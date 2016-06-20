#!/usr/bin/env ruby
# Solution for Hamming
# Written by Sofia Nieves
# Mon 20 Jun 05:20:42 UTC 2016
#

class Hamming
  def self.compute(strand1, strand2)
    distance = 0

    if strand1.length != strand2.length
      raise ArgumentError
    end

    for i in 0..strand1.length
      if strand1[i] != strand2[i]
        distance += 1
      end
    end

    return distance
  end
end
